from django.db.models import QuerySet

from main.dao.banknote_dao import BanknoteDAO
from main.services.base_service import BaseService


class BanknoteService(BaseService):
    """Сервис для работы с данными банкнот.

    Наследует базовый функционал от BaseService и использует BanknoteDAO для доступа к данным.
    """

    def __init__(self) -> None:
        """Инициализация сервиса.

        Создаёт экземпляр BanknoteDAO для работы с данными банкнот.
        """
        super().__init__(BanknoteDAO())

    def get_all(self) -> QuerySet:
        """Возвращает QuerySet из экземпляров класса Banknote с оптимизированными запросами."""
        return (
            self.dao.get_all()
            .select_related("country", "material", "state", "type_of_edition")
            .prefetch_related("themes")
        )
