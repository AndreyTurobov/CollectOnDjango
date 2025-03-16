from django.views.generic import CreateView

from main.forms.collection_form import CollectionForm


class CollectionCreateController(CreateView):
    """Контроллер для создания новой коллекции."""

    form_class = CollectionForm
    template_name = "collections/create_collection.html"
    success_url = "/collections/list/"

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавление коллекции"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Коллекции", "url": "/collections/list/"},
            {"title": "Создать коллекцию", "url": ""},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет коллекцию в базе данных."""
        return super().form_valid(form)
