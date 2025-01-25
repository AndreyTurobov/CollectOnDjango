from ..models.banknote import Banknote


class BanknoteDAO:
    @staticmethod
    def get_all_banknotes():
        return Banknote.objects.all()

    @staticmethod
    def get_banknote_by_id(pk):
        return Banknote.objects.get(pk=pk)

    @staticmethod
    def search_banknotes(filters):
        """
        Реализация фильтрации банкнот на уровне данных.
        :param filters: Словарь с параметрами фильтрации.
        :return: Отфильтрованный QuerySet банкнот.
        """
        return Banknote.objects.filter(**filters)
