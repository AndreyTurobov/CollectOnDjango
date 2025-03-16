from typing import TypeVar

from django.db.models import (
    Model,
    QuerySet,
)
from django.views.generic import ListView

from main.services.collection_service import CollectionService

T = TypeVar("T", bound=Model)


class CollectionListController(ListView):
    """Контроллер для отображения списка коллекций.

    Использует сервис для получения списка коллекций.
    """

    template_name = "collections/list_collections.html"
    context_object_name = "collections"
    paginate_by = 4

    def __init__(self, *args, **kwargs):
        """Инициализация контроллера.

        Создаёт экземпляр CollectionService для работы с данными коллекций.
        """
        super().__init__(*args, **kwargs)
        self.service = CollectionService()

    def get_context_data(self, **kwargs) -> None:
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Коллекции"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Коллекции", "url": ""},
        ]
        return context

    def get_queryset(self) -> QuerySet[T]:
        """Возвращает список коллекций."""
        return self.service.get_all()
