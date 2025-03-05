from typing import (
    Any,
    Generic,
    Optional,
    TypeVar,
)

from django.db.models import (
    Model,
    QuerySet,
)

# Определяем типовую переменную для модели
T = TypeVar("T", bound=Model)


class BaseDAO(Generic[T]):
    """Базовый DAO для работы с данными.

    Предоставляет общие методы для получения, поиска, обновления и удаления объектов.
    """

    def __init__(self, model: type[T]) -> None:
        """Инициализация DAO.

        :param model: Модель Django, с которой будет работать DAO.
        """
        self.model = model

    def get_all(self) -> QuerySet[T]:
        """Возвращает все объекты.

        :return: QuerySet всех объектов.
        """
        return self.model.objects.all()

    def get_by_slug(self, slug: str) -> Optional[T]:
        """Возвращает объект по его slug.

        :param slug: Уникальный слаг объекта.
        :return: Объект или None, если объект не найден.
        """
        try:
            return self.model.objects.get(slug=slug)
        except self.model.DoesNotExist:
            return None

    def get_by_filter(self, filters: dict[str, Any]) -> QuerySet[T]:
        """Возвращает отфильтрованные объекты на основе переданных параметров.

        :param filters: Словарь с параметрами фильтрации.
        :return: QuerySet отфильтрованных объектов.
        """
        filters = {k: v for k, v in filters.items() if v}
        return self.model.objects.filter(**filters)

    def get_new_items(self) -> QuerySet[T]:
        """Возвращает QuerySet объектов, отсортированный по дате создания (самые новые)."""
        return self.model.objects.filter(in_collect=True).order_by("-created_at").all()

    def get_planned_items(self) -> QuerySet[T]:
        """Возвращает QuerySet объектов каталога, планируемых к приобретению в коллекцию."""
        return self.model.objects.filter(in_collect=False).order_by("-created_at").all()
