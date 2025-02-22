from django.views.generic import CreateView

from main.forms.choices_forms import TypeOfEditionForm


class TypeOfEditionCreateController(CreateView):
    form_class = TypeOfEditionForm
    template_name = "choices/create_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
