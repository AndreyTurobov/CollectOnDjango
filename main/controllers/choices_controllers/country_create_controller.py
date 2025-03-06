from django.views.generic import CreateView

from main.forms.choices_forms import CountryForm


class CountryCreateController(CreateView):
    form_class = CountryForm
    template_name = "choices/create_form.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавление страны"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Добавление страны", "url": ""},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет данные о стране в базе данных."""
        form.save()
        return super().form_valid(form)
