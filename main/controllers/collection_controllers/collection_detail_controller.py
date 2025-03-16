from django.views.generic import DetailView

from main.services.collection_service import CollectionService


class CollectionDetailController(DetailView):
    """Контроллер для отображения детальной информации о коллекции.

    Использует сервис для получения коллекции с предзагруженными монетами и банкнотами.
    """

    template_name = "collections/detail_collections.html"
    context_object_name = "collection"
    slug_url_kwarg = "slug"

    def __init__(self, *args, **kwargs):
        """Инициализация контроллера.

        Создаёт экземпляр CollectionService для работы с данными коллекций.
        """
        super().__init__(*args, **kwargs)
        self.service = CollectionService()

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        collection = self.get_object()
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Коллекции", "url": "/collections/"},
            {"title": collection.title, "url": ""},
        ]
        return context

    def get_object(self, queryset=None):
        """Возвращает коллекцию с предзагруженными монетами и банкнотами."""
        return self.service.get_by_slug_with_items(self.kwargs[self.slug_url_kwarg])
