from django.db.models import QuerySet

from main.controllers.coin_controllers.coin_list_controller import CoinListController


class CoinPlannedController(CoinListController):
    """Контроллер для отображения монет которые планируется добавить в коллекцию.

    Использует CoinService для получения данных.
    """

    template_name = "coins/plan_coins.html"

    def get_queryset(self) -> QuerySet:
        """Возвращает QuerySet монет, которые планируются добавить в коллекцию."""
        qs = self.service.get_planned_items()
        return qs

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Планируемые монеты"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Монеты", "url": "/coins/"},
            {"title": "Планируемые монеты", "url": ""},
        ]
        return context
