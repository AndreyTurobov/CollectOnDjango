from ..models.coin import Coin


class CoinDAO:
    @staticmethod
    def get_all_coins():
        return Coin.objects.all()

    @staticmethod
    def get_coin_by_id(pk):
        return Coin.objects.get(pk=pk)

    @staticmethod
    def search_coins(filters):
        """
        Реализация фильтрации монет на уровне данных.
        :param filters: Словарь с параметрами фильтрации.
        :return: Отфильтрованный QuerySet монет.
        """
        return Coin.objects.filter(**filters)
