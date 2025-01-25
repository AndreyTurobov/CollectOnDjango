from django.views.generic import ListView, DetailView
from ..services.banknote_service import BanknoteService


class BanknoteListView(ListView):
    template_name = 'banknotes/list.html'
    context_object_name = 'banknotes'
    paginate_by = 9

    def get_queryset(self):
        return BanknoteService.get_all_banknotes().order_by('id')


class BanknoteDetailView(DetailView):
    template_name = 'banknotes/detail.html'
    context_object_name = 'banknote'

    def get_object(self, queryset=None):
        return BanknoteService.get_banknote_by_id(self.kwargs['pk'])
