from main.dao.base_dao import BaseDAO
from main.models.banknote_model import BanknoteModel as Banknote


class BanknoteDAO(BaseDAO[Banknote]):
    """
    DAO для работы с данными банкнот.

    Наследует базовый функционал от BaseDAO и работает с моделью Banknote.
    """

    def __init__(self) -> None:
        """
        Инициализация DAO.

        Указывает модель Banknote для работы с данными.
        """
        super().__init__(Banknote)
