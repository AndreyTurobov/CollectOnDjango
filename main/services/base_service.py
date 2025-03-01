from typing import (
    Any,
    Generic,
    Optional,
    TypeVar,
)

from django.db.models.query import QuerySet

# Определяем типовую переменную для модели
T = TypeVar("T")


class BaseService(Generic[T]):
    """Базовый сервис для работы с данными.

    Предоставляет общие методы для получения, поиска, обновления и удаления объектов.
    """

    def __init__(self, dao) -> None:
        """Инициализация сервиса.

        :param dao: Объект DAO, который будет использоваться для доступа к данным.
        """
        self.dao = dao

    def get_all(self) -> QuerySet[T]:
        """Возвращает все объекты.

        :return: QuerySet всех объектов.
        """
        return self.dao.get_all()

    def get_by_slug(self, slug: str) -> Optional[T]:
        """Возвращает объект по его slug.

        :param slug: Уникальный слаг объекта.
        :return: Объект или None, если объект не найден.
        """
        return self.dao.get_by_slug(slug)

    def get_by_filter(self, filters: dict[str, Any]) -> QuerySet[T]:
        """Возвращает отфильтрованные объекты на основе переданных параметров.

        :param filters: Словарь с параметрами фильтрации.
        :return: QuerySet отфильтрованных объектов.
        """
        return self.dao.get_by_filter(filters)

    def get_new_items(self, *args, **kwargs) -> list[T]:
        """Возвращает новые объекты.

        :return: list новых объектов.
        """
        return self.dao.get_new(*args, **kwargs)

    def get_planned_items(self, *args, **kwargs) -> list[T]:
        """Возвращает планируемые к приобретению объекты.

        :return: list планируемых объектов.
        """
        return self.dao.get_planned(*args, **kwargs)
