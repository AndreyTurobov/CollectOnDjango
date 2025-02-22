from django.db.models.aggregates import Count
from django.db.models.query import QuerySet

from main.dao.material_dao import MaterialDAO


class MaterialService:
    """Сервис для работы с материалами.

    Наследует базовый функционал от BaseService и использует MaterialDAO для доступа к данным.
    """

    def __init__(self):
        """Инициализация сервиса.

        Создает экземпляр MaterialDAO для доступа к данным.
        """
        self.dao = MaterialDAO()

    def get_annotated_materials(self) -> QuerySet:
        """Возвращает материалы с аннотацией item_count."""
        return self.dao.model.objects.annotate(
            item_count=Count("coinmodel") + Count("banknotemodel")
        ).filter(item_count__gt=0)
