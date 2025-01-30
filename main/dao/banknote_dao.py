from main.dao.base_dao import BaseDAO
from main.models.banknote_model import BanknoteModel as Banknote


class BanknoteDAO(BaseDAO[Banknote]):
    def __init__(self):
        super().__init__(Banknote)
