from django.db.models import QuerySet

from main.controllers.banknote_controllers.banknote_list_controller import BanknoteListController
from main.services.banknote_service import BanknoteService


class BanknotePlannedController(BanknoteListController):
    """Контроллер для отображения монет которые планируется добавить в коллекцию.

    Использует CoinService для получения данных.
    """

    template_name = "banknotes/plan_banknotes.html"
    service = BanknoteService()

    def get_queryset(self) -> QuerySet:
        """Возвращает QuerySet монет, которые планируются добавить в коллекцию."""
        qs = self.service.get_planned_items()
        return qs

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Планируемые банкноты"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Банкноты", "url": "/banknotes/"},
            {"title": "Планируемые банкноты", "url": ""},
        ]
        return context
