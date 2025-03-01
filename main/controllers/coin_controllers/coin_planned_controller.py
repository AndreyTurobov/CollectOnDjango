from django.views.generic import ListView

from main.services.coin_service import CoinService


class CoinPlannedController(ListView):
    """Контроллер для отображения монет которые планируется добавить в коллекцию.

    Использует CoinService для получения данных.
    """

    template_name = "coins/coin_planned.html"
    context_object_name = "coins"
    service = CoinService()

    def get_queryset(self) -> list:
        """Возвращает монеты которые планируется добавить в коллекцию."""
        return self.service.get_planned_items()
