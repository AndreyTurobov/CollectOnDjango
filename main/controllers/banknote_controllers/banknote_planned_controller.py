from django.db.models import QuerySet

from main.controllers.banknote_controllers.banknote_list_controller import BanknoteListController


class BanknotePlannedController(BanknoteListController):
    """Контроллер для отображения монет которые планируется добавить в коллекцию.

    Использует CoinService для получения данных.
    """

    template_name = "banknotes/plan_banknotes.html"

    def get_queryset(self) -> QuerySet:
        """Возвращает QuerySet монет, которые планируются добавить в коллекцию."""
        qs = self.service.get_planned_items()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Планируемые банкноты"
        return context
