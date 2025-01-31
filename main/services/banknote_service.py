from main.dao.banknote_dao import BanknoteDAO
from main.services.base_service import BaseService


class BanknoteService(BaseService):
    """
    Сервис для работы с данными банкнот.

    Наследует базовый функционал от BaseService и использует BanknoteDAO для доступа к данным.
    """

    def __init__(self):
        """
        Инициализация сервиса.

        Создаёт экземпляр BanknoteDAO для работы с данными банкнот.
        """
        super().__init__(BanknoteDAO())
