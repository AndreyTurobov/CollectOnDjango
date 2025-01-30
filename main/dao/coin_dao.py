from main.dao.base_dao import BaseDAO
from main.models.coin_model import CoinModel as Coin


class CoinDAO(BaseDAO[Coin]):
    def __init__(self):
        super().__init__(Coin)
