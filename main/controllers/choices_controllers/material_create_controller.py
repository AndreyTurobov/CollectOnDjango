from django.views.generic import CreateView

from main.forms.choices_forms import MaterialForm


class MaterialCreateController(CreateView):
    form_class = MaterialForm
    template_name = "choices/create_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
