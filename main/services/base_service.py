from typing import Dict, Any, TypeVar

from django.db.models import QuerySet

# Определяем типовую переменную для модели
T = TypeVar('T')


class BaseService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self) -> QuerySet[T]:
        """Получить все объекты."""
        return self.dao.get_all()

    def get_by_id(self, pk: int) -> T:
        """Получить объект по его ID."""
        return self.dao.get_by_id(pk)

    def get_by_filter(self, filters: Dict[str, Any]) -> QuerySet[T]:
        """
        Фильтрация объектов на основе переданных параметров.
        :param filters: Словарь с параметрами фильтрации.
        :return: Отфильтрованный QuerySet.
        """
        return self.dao.get_by_filter(filters)
