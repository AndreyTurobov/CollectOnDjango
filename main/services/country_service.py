from django.db.models.aggregates import Count
from django.db.models.query import QuerySet

from main.dao.country_dao import CountryDAO


class CountryService:
    """Сервис для работы с данными стран.

    Наследует базовый функционал от BaseService и использует CountryDAO для доступа к данным.
    """

    def __init__(self):
        """Инициализация сервиса.

        Создаёт экземпляр CountryDAO для работы с данными стран.
        """
        self.dao = CountryDAO()

    def get_annotated_countries(self) -> QuerySet:
        """Возвращает страны с аннотацией item_count."""
        return self.dao.model.objects.annotate(
            item_count=Count("coinmodel") + Count("banknotemodel")
        ).filter(item_count__gt=0)
