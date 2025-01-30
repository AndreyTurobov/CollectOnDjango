from main.dao.banknote_dao import BanknoteDAO
from main.services.base_service import BaseService


class BanknoteService(BaseService):
    def __init__(self):
        super().__init__(BanknoteDAO())
