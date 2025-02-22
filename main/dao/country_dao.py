from main.dao.base_dao import BaseDAO
from main.models.choice_models import Country


class CountryDAO(BaseDAO):
    """DAO для работы с данными стран.

    Наследует базовый функционал от BaseDAO и работает с моделью Country.
    """

    def __init__(self):
        """Инициализация DAO.

        Указывает модель Country для работы с данными.
        """
        super().__init__(Country)
