from typing import Optional

from django.db.models import QuerySet

from main.dao.base_dao import BaseDAO
from main.models.banknote_model import BanknoteModel
from main.models.coin_model import CoinModel
from main.models.collection_model import (
    CollectionBanknoteModel,
    CollectionCoinModel,
    CollectionModel,
)


class CollectionDAO(BaseDAO[CollectionModel]):
    """DAO для работы с данными коллекций.

    Наследует базовый функционал от BaseDAO и работает с моделью Collection.
    """

    def __init__(self):
        """Инициализация DAO.

        Указывает модель Collection для работы с данными.
        """
        super().__init__(CollectionModel)

    def get_all(self) -> QuerySet[CollectionModel]:
        """Возвращает все коллекции в порядке убывания даты создания."""
        return self.model.objects.all().order_by("-created_at")

    def get_by_slug(self, slug: str) -> Optional[CollectionModel]:
        """Возвращает коллекцию по её slug."""
        try:
            return self.model.objects.get(slug=slug)
        except self.model.DoesNotExist:
            return None

    def add_banknote(self, collection: CollectionModel, banknote: BanknoteModel) -> None:
        """Добавляет банкноту в коллекцию через промежуточную модель."""
        CollectionBanknoteModel.objects.get_or_create(collection=collection, banknote=banknote)
        # Обновляем флаг in_collect у банкноты
        banknote.in_collect = True
        banknote.save()

    def add_coin(self, collection: CollectionModel, coin: CoinModel) -> None:
        """Добавляет монету в коллекцию через промежуточную модель."""
        CollectionCoinModel.objects.get_or_create(collection=collection, coin=coin)
        # Обновляем флаг in_collect у монеты
        coin.in_collect = True
        coin.save()
