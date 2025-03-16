from main.dao.collection_dao import CollectionDAO
from main.services.base_service import BaseService


class CollectionService(BaseService):
    """Сервис для работы с данными коллекций.

    Наследует базовый функционал от BaseService и работает с моделью CollectionModel.
    """

    def __init__(self):
        """Инициализация сервиса.

        Создаёт экземпляр CollectionDAO для работы с данными коллекций.
        """
        super().__init__(CollectionDAO())

    def get_by_slug_with_items(self, slug: str):
        """Возвращает коллекцию с предзагруженными монетами и банкнотами."""
        return self.dao.model.objects.prefetch_related("coins", "banknotes").get(slug=slug)
