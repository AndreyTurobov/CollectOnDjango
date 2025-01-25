from django.views.generic import ListView, DetailView

from ..services.coin_service import CoinService


class CoinListView(ListView):
    template_name = 'coins/list.html'
    context_object_name = 'coins'
    paginate_by = 9

    def get_queryset(self):
        return CoinService.get_all_coins().order_by('id')


class CoinDetailView(DetailView):
    template_name = 'coins/detail.html'
    context_object_name = 'coin'

    def get_object(self, queryset=None):
        return CoinService.get_coin_by_id(self.kwargs['pk'])