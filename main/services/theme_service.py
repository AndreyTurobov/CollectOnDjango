from django.db.models.aggregates import Count
from django.db.models.query import QuerySet

from main.dao.theme_dao import ThemeDAO


class ThemeService:
    """Сервис для работы с темами.

    Наследует базовый функционал от BaseService и использует ThemeDAO для доступа к данным.
    """

    def __init__(self):
        """Инициализация сервиса.

        Создает экземпляр ThemeDAO для доступа к данным.
        """
        self.dao = ThemeDAO()

    def get_annotated_themes(self) -> QuerySet:
        """Возвращает темы с аннотацией item_count."""
        return self.dao.model.objects.annotate(
            item_count=Count("coinmodel") + Count("banknotemodel")
        ).filter(item_count__gt=0)
