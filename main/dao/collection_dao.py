from typing import Optional

from django.db.models import QuerySet

from main.dao.base_dao import BaseDAO
from main.models.collection_model import CollectionModel as Collection


class CollectionDAO(BaseDAO[Collection]):
    """DAO для работы с данными коллекций.

    Наследует базовый функционал от BaseDAO и работает с моделью Collection.
    """

    def __init__(self):
        """Инициализация DAO.

        Указывает модель Collection для работы с данными.
        """
        super().__init__(Collection)

    def get_all(self) -> QuerySet[Collection]:
        """Возвращает все коллекции в порядке убывания даты создания."""
        return self.model.objects.all().order_by("-created_at")

    def get_by_slug(self, slug: str) -> Optional[Collection]:
        """Возвращает коллекцию по её slug."""
        try:
            return self.model.objects.get(slug=slug)
        except self.model.DoesNotExist:
            return None
