from django.views.generic import CreateView

from main.forms.banknote_form import BanknoteForm


class BanknoteCreateController(CreateView):
    form_class = BanknoteForm
    template_name = "banknotes/create_banknote.html"
    success_url = "/banknotes/"

    def form_valid(self, form):
        banknote = form.save(commit=False)
        banknote.save()
        return super().form_valid(form)
