from main.dao.base_dao import BaseDAO
from main.models.choice_models import Material


class MaterialDAO(BaseDAO):
    """DAO для работы с данными материалов.

    Наследует базовый функционал от BaseDAO и работает с моделью Material.
    """

    def __init__(self):
        """Инициализация DAO.

        Указывает модель Material для работы с данными.
        """
        super().__init__(Material)
