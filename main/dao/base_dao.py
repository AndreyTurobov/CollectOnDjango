from typing import Type, Generic, Dict, Any, TypeVar

from django.db.models import Model, QuerySet

# Определяем типовую переменную для модели
T = TypeVar('T', bound=Model)


class BaseDAO(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def get_all(self) -> QuerySet[T]:
        """Получить все объекты."""
        return self.model.objects.all()

    def get_by_id(self, pk: int) -> T:
        """Получить объект по его ID."""
        return self.model.objects.get(pk=pk)

    def get_by_filter(self, filters: Dict[str, Any]) -> QuerySet[T]:
        """
        Фильтрация объектов на основе переданных параметров.
        :param filters: Словарь с параметрами фильтрации.
        :return: Отфильтрованный QuerySet.
        """
        # Убираем пустые параметры
        filters = {k: v for k, v in filters.items() if v}
        return self.model.objects.filter(**filters)
