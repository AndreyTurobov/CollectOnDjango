from django.views.generic import CreateView

from main.forms.choices_forms import MaterialForm


class MaterialCreateController(CreateView):
    form_class = MaterialForm
    template_name = "choices/create_form.html"
    success_url = "/"

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Материал"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Материал", "url": ""},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет объект в базе данных."""
        form.save()
        return super().form_valid(form)
