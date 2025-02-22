from django.db.models.aggregates import Count
from django.db.models.query import QuerySet

from main.dao.type_of_edition_dao import TypeOfEditionDAO


class TypeOfEditionService:
    """Сервис для работы с типами издания.

    Наследует базовый функционал от BaseService и использует TypeOfEditionDAO для доступа к данным.
    """

    def __init__(self):
        """Инициализация сервиса.

        Создает экземпляр TypeOfEditionDAO для доступа к данным.
        """
        self.dao = TypeOfEditionDAO()

    def get_annotated_type_of_editions(self) -> QuerySet:
        """Возвращает типы издания с аннотацией item_count."""
        return self.dao.model.objects.annotate(
            item_count=Count("coinmodel") + Count("banknotemodel")
        ).filter(item_count__gt=0)
