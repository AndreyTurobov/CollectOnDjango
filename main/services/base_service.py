from typing import (
    Any,
    TypeVar,
)

from django.db.models import QuerySet

# Определяем типовую переменную для модели
T = TypeVar('T')


class BaseService:
    """
    Базовый сервис для работы с данными.

    Предоставляет общие методы для получения, поиска, обновления и удаления объектов.
    """
    def __init__(self, dao):
        """
        Инициализация сервиса.

        :param dao: Объект DAO, который будет использоваться для доступа к данным.
        """
        self.dao = dao
    def get_all(self) -> QuerySet[T]:
        """
        Возвращает все объекты.

        :return: QuerySet всех объектов.
        """
        return self.dao.get_all()

    def get_by_id(self, pk: int) -> T:
        """
        Возвращает объект по его ID.

        :param pk: ID объекта.
        :return: Объект или None, если объект не найден.
        """
        return self.dao.get_by_id(pk)

    def get_by_filter(self, filters: dict[str, Any]) -> QuerySet[T]:
        """
        Возвращает отфильтрованные объекты на основе переданных параметров.

        :param filters: Словарь с параметрами фильтрации.
        :return: QuerySet отфильтрованных объектов.
        """
        return self.dao.get_by_filter(filters)
