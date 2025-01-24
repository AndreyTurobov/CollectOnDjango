from django.views.generic import ListView
from ..services.coin_service import CoinService


class CoinListView(ListView):
    template_name = 'coins/list.html'
    context_object_name = 'coins'
    paginate_by = 9

    def get_queryset(self):
        return CoinService.get_all_coins().order_by('id')
