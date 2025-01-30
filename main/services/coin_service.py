from main.dao.coin_dao import CoinDAO
from main.services.base_service import BaseService


class CoinService(BaseService):
    def __init__(self):
        super().__init__(CoinDAO())
