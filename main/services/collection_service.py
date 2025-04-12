from django.db import transaction

from main.dao.collection_dao import CollectionDAO
from main.services.banknote_service import BanknoteService
from main.services.base_service import BaseService
from main.services.coin_service import CoinService


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

    @transaction.atomic
    def add_banknote_to_collection(self, collection_slug: str, banknote_slug: str) -> None:
        collection = self.get_by_slug(collection_slug)
        banknote = BanknoteService().get_by_slug(banknote_slug)
        if collection and banknote:
            self.dao.add_banknote(collection, banknote)

    @transaction.atomic
    def add_coin_to_collection(self, collection_slug: str, coin_slug: str) -> None:
        collection = self.get_by_slug(collection_slug)
        coin = CoinService().get_by_slug(coin_slug)
        if collection and coin:
            self.dao.add_coin(collection, coin)
