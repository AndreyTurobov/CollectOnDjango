from django.views.generic import ListView

from main.services.banknote_service import BanknoteService


class BanknotePlannedController(ListView):
    """Контроллер для отображения банкнот, которые планируются добавить в коллекцию.

    Использует BanknoteService для получения данных.
    """

    template_name = "banknotes/banknote_planned.html"
    context_object_name = "banknotes"
    service = BanknoteService()

    def get_queryset(self) -> list:
        """Возвращает банкноты, которые планируются добавить в коллекцию."""
        return self.service.get_planned_items()
