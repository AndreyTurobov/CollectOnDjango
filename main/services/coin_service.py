from django.db.models import QuerySet

from main.dao.coin_dao import CoinDAO
from main.services.base_service import BaseService


class CoinService(BaseService):
    """Сервис для работы с данными монет.

    Наследует базовый функционал от BaseService и использует CoinDAO для доступа к данным.
    """

    def __init__(self) -> None:
        """Инициализация сервиса.

        Создаёт экземпляр CoinDAO для работы с данными монет.
        """
        super().__init__(CoinDAO())

    def get_all(self) -> QuerySet:
        """Возвращает QuerySet из экземпляров класса Coin с оптимизированными запросами."""
        return (
            self.dao.get_all()
            .select_related("country", "material", "state", "type_of_edition")
            .prefetch_related("themes")
        )
