from django.views.generic import UpdateView

from main.services.banknote_service import BanknoteService


class BanknoteUpdateController(UpdateView):
    template_name = "banknotes/update_banknote.html"
    success_url = "/banknotes/"

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр BanknoteService для работы с данными банкнот.
        """
        super().__init__(*args, **kwargs)
        self.service = BanknoteService()

    def get_object(self, queryset=None):
        return self.service.get_by_slug(self.kwargs["slug"])

    def form_valid(self, form):
        self.service.update(self.kwargs["slug"], form.cleaned_data)
        return super().form_valid(form)
