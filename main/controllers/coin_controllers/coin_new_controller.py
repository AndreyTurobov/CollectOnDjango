from django.views.generic import ListView

from main.services.coin_service import CoinService


class CoinNewController(ListView):
    """Контроллер для отображения последних 10 монет, добавленных в коллекцию.

    Использует CoinService для получения данных.
    """

    template_name = "coins/new_coins.html"
    context_object_name = "coins"
    paginate_by = 9
    service = CoinService()

    def get_queryset(self):
        """Возвращает последние 10 монет, добавленных в коллекцию."""
        return self.service.get_new_items()
