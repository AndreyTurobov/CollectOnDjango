from django.views.generic import ListView
from ..services.banknote_service import BanknoteService


class BanknoteListView(ListView):
    template_name = 'banknotes/list.html'
    context_object_name = 'banknotes'
    paginate_by = 9

    def get_queryset(self):
        return BanknoteService.get_all_banknotes().order_by('id')
