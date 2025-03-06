from django.views.generic import CreateView

from main.forms.choices_forms import StateForm


class StateCreateController(CreateView):
    form_class = StateForm
    template_name = "choices/create_form.html"
    success_url = "/"

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить состояние"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Состояния", "url": "/choices/state"},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет данные объекта в базе данных."""
        form.save()
        return super().form_valid(form)
