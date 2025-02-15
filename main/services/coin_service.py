from main.dao.coin_dao import CoinDAO
from main.services.base_service import BaseService


class CoinService(BaseService):
    """
    Сервис для работы с данными монет.

    Наследует базовый функционал от BaseService и использует CoinDAO для доступа к данным.
    """

    def __init__(self) -> None:
        """
        Инициализация сервиса.

        Создаёт экземпляр CoinDAO для работы с данными монет.
        """
        super().__init__(CoinDAO())
