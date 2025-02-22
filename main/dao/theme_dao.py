from main.dao.base_dao import BaseDAO
from main.models.choice_models import Theme


class ThemeDAO(BaseDAO):
    """DAO для работы с темами.

    Наследует базовый функционал от BaseDAO и работает с моделью Theme.
    """

    def __init__(self):
        """Инициализация DAO.

        Указывает модель Theme для работы с данными.
        """
        super().__init__(Theme)
