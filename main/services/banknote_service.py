from ..dao.banknote_dao import BanknoteDAO


class BanknoteService:
    @staticmethod
    def get_all_banknotes():
        return BanknoteDAO.get_all_banknotes()

    @staticmethod
    def get_banknote_by_id(pk):
        return BanknoteDAO.get_banknote_by_id(pk)

    @staticmethod
    def search_banknotes(filters):
        """
        Use Case: Фильтрация банкнот на основе переданных параметров.
        :param filters: Словарь с параметрами фильтрации.
        :return: Отфильтрованный QuerySet банкнот.
        """
        # Убираем пустые параметры
        filters = {k: v for k, v in filters.items() if v}
        # Передаём параметры фильтрации в DAO
        return BanknoteDAO.search_banknotes(filters)
