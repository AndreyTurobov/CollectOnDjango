from ..dao.coin_dao import CoinDAO


class CoinService:
    @staticmethod
    def get_all_coins():
        return CoinDAO.get_all_coins()

    @staticmethod
    def get_coin_by_id(pk):
        return CoinDAO.get_coin_by_id(pk)

    @staticmethod
    def search_coins(**filters):
        return CoinDAO.search_coins(**filters)
