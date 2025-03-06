from django.views.generic import CreateView

from main.forms.choices_forms import TypeOfEditionForm


class TypeOfEditionCreateController(CreateView):
    form_class = TypeOfEditionForm
    template_name = "choices/create_form.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Тип выпуска"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Тип выпуска", "url": ""},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет объект в базе данных."""
        form.save()
        return super().form_valid(form)
