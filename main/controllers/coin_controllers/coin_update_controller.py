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

    def form_valid(self, form):
        self.service.update(self.kwargs["slug"], form.cleaned_data)
        return super().form_valid(form)
