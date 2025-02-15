from main.dao.base_dao import BaseDAO
from main.models.coin_model import CoinModel as Coin


class CoinDAO(BaseDAO[Coin]):
    """
    DAO для работы с данными монет.

    Наследует базовый функционал от BaseDAO и работает с моделью Coin.
    """

    def __init__(self) -> None:
        """
        Инициализация DAO.

        Указывает модель Coin для работы с данными.
        """
        super().__init__(Coin)
