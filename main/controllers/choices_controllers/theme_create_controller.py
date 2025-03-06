from django.views.generic import CreateView

from main.forms.choices_forms import ThemeForm


class ThemeCreateController(CreateView):
    form_class = ThemeForm
    template_name = "choices/create_form.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Создание темы"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Темы", "url": "/themes/"},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет объект в базе данных."""
        form.save()
        return super().form_valid(form)
