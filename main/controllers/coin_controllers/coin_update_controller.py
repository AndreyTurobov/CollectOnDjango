from django.views.generic import UpdateView

from main.forms.coin_form import CoinForm
from main.services.coin_service import CoinService


class CoinUpdateController(UpdateView):
    template_name = "coins/update_coin.html"
    success_url = "/coins/"
    form_class = CoinForm

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр CoinService для работы с данными монет.
        """
        super().__init__(*args, **kwargs)
        self.service = CoinService()

    def get_object(self, queryset=None):
        return self.service.get_by_slug(self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        coin = self.get_object()
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Монеты", "url": "/coins/"},
            {"title": f"Редактировать монету: {coin.full_title}", "url": ""},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет изменения в данных о монете."""
        self.object = form.save()
        return super().form_valid(form)
