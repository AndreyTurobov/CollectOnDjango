from django.db.models.aggregates import Count
from django.db.models.query import QuerySet

from main.dao.state_dao import StateDAO


class StateService:
    """Сервис для работы с состояниями.

    Наследует базовый функционал от BaseService и использует StateDAO для доступа к данным.
    """

    def __init__(self):
        """Инициализация сервиса.

        Создает экземпляр StateDAO для доступа к данным.
        """
        self.dao = StateDAO()

    def get_annotated_states(self) -> QuerySet:
        """Возвращает состояния с аннотацией item_count."""
        return self.dao.model.objects.annotate(
            item_count=Count("coinmodel") + Count("banknotemodel")
        ).filter(item_count__gt=0)
