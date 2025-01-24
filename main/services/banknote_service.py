from ..dao.banknote_dao import BanknoteDAO


class BanknoteService:
    @staticmethod
    def get_all_banknotes():
        return BanknoteDAO.get_all_banknotes()

    @staticmethod
    def get_banknote_by_id(pk):
        return BanknoteDAO.get_banknote_by_id(pk)

    @staticmethod
    def search_banknotes(**filters):
        return BanknoteDAO.search_banknotes(**filters)
