from django.views.generic import CreateView

from main.forms.coin_form import CoinForm


class CoinCreateController(CreateView):
    form_class = CoinForm
    template_name = "coins/create_coin.html"
    success_url = "/coins/"

    def form_valid(self, form):
        coin = form.save(commit=False)
        coin.save()
        return super().form_valid(form)
