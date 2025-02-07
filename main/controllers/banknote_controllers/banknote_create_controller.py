from django.views.generic import CreateView

from main.forms.banknote_form import BanknoteForm
from main.services.banknote_service import BanknoteService


class BanknoteCreateController(CreateView):
    form_class = BanknoteForm
    template_name = "banknotes/create_banknote.html"
    success_url = "/banknotes/"

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр BanknoteService для работы с данными банкнот.
        """
        super().__init__(*args, **kwargs)
        self.service = BanknoteService()

    def form_valid(self, form):
        self.service.create(form.cleaned_data)
        return super().form_valid(form)
