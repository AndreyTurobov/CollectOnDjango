from django.views.generic import UpdateView

from main.forms.collection_form import CollectionForm
from main.services.collection_service import CollectionService


class CollectionUpdateController(UpdateView):
    """Контроллер для создания новой коллекции."""

    form_class = CollectionForm
    template_name = "collections/update_collection.html"
    success_url = "/collections/list/"

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр CollectionService для работы с данными коллекций.
        """
        super().__init__(*args, **kwargs)
        self.service = CollectionService()

    def get_object(self, queryset=None):
        return self.service.get_by_slug(self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        collection = self.get_object()
        context["title"] = "Редактирование коллекции"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Коллекции", "url": "/collections/list/"},
            {"title": f"Редактировать коллекцию: {collection.title}", "url": ""},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет изменения в данных о коллекции."""
        self.object = form.save()
        return super().form_valid(form)
