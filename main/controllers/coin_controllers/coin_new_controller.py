from django.db.models import QuerySet

from main.controllers.coin_controllers.coin_list_controller import CoinListController
from main.services.coin_service import CoinService


class CoinNewController(CoinListController):
    """Контроллер для отображения монет которые планируется добавить в коллекцию.

    Использует CoinService для получения данных.
    """

    template_name = "coins/new_coins.html"
    service = CoinService()

    def get_queryset(self) -> QuerySet:
        """Возвращает QuerySet монет, которые планируются добавить в коллекцию."""
        qs = self.service.get_new_items()
        return qs

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Новые монеты"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Монеты", "url": "/coins/"},
            {"title": "Новые монеты", "url": ""},
        ]
        return context
