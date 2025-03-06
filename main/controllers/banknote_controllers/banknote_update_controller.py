from django.views.generic import UpdateView

from main.forms.banknote_form import BanknoteForm
from main.services.banknote_service import BanknoteService


class BanknoteUpdateController(UpdateView):
    template_name = "banknotes/update_banknote.html"
    success_url = "/banknotes/"
    form_class = BanknoteForm

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр BanknoteService для работы с данными банкнот.
        """
        super().__init__(*args, **kwargs)
        self.service = BanknoteService()

    def get_object(self, queryset=None):
        return self.service.get_by_slug(self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        banknote = self.get_object()
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Банкноты", "url": "/banknotes/"},
            {"title": f"Редактировать банкноту: {banknote.full_title}", "url": ""},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет изменения в данных о банкноте."""
        self.object = form.save()
        return super().form_valid(form)
