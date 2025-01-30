from django.views.generic import DetailView

from main.services.banknote_service import BanknoteService


class BanknoteDetailController(DetailView):
    template_name = 'banknotes/detail.html'
    context_object_name = 'banknote'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = BanknoteService()

    def get_object(self, queryset=None):
        return self.service.get_by_id(self.kwargs['pk'])
