from django.views.generic import DetailView

from main.services.coin_service import CoinService


class CoinDetailController(DetailView):
    template_name = 'coins/detail.html'
    context_object_name = 'coin'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = CoinService()

    def get_object(self, queryset=None):
        return self.service.get_by_id(self.kwargs['pk'])
