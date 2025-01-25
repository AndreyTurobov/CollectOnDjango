from ..dao.coin_dao import CoinDAO


class CoinService:
    @staticmethod
    def get_all_coins():
        return CoinDAO.get_all_coins()

    @staticmethod
    def get_coin_by_id(pk):
        return CoinDAO.get_coin_by_id(pk)

    @staticmethod
    def search_coins(filters):
        """
        Use Case: Фильтрация монет на основе переданных параметров.
        :param filters: Словарь с параметрами фильтрации.
        :return: Отфильтрованный QuerySet монет.
        """
        # Убираем пустые параметры
        filters = {k: v for k, v in filters.items() if v}
        # Передаём параметры фильтрации в DAO
        return CoinDAO.search_coins(filters)
