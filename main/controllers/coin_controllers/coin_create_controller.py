from django.views.generic import CreateView

from main.forms.coin_form import CoinForm
from main.services.coin_service import CoinService


class CoinCreateController(CreateView):
    form_class = CoinForm
    template_name = "coins/create_coin.html"
    success_url = "/coins/"

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр CoinService для работы с данными монет.
        """
        super().__init__(*args, **kwargs)
        self.service = CoinService()

    def form_valid(self, form):
        self.service.create(form.cleaned_data)
        return super().form_valid(form)
