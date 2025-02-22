from main.dao.base_dao import BaseDAO
from main.models.choice_models import State


class StateDAO(BaseDAO):
    """DAO для работы с данными состояний.

    Наследует базовый функционал от BaseDAO и работает с моделью State.
    """

    def __init__(self):
        """Инициализация DAO.

        Указывает модель State для работы с данными.
        """
        super().__init__(State)
