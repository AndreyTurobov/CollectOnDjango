from django.views.generic import ListView

from main.models.choice_models import Country


class CountryListController(ListView):
    model = Country
    template_name = "countries/countries_list.html"
    context_object_name = "countries"

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Страны"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Страны", "url": ""},
        ]
        return context
