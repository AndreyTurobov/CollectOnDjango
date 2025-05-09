from main.dao.base_dao import BaseDAO
from main.models.choice_models import TypeOfEdition


class TypeOfEditionDAO(BaseDAO):
    """DAO для работы с данными типа издания.

    Наследует базовый функционал от BaseDAO и работает с моделью TypeOfEdition.
    """

    def __init__(self):
        """Инициализация DAO.

        Указывает модель TypeOfEdition для работы с данными.
        """
        super().__init__(TypeOfEdition)
