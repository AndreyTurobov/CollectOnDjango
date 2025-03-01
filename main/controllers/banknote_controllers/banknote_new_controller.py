from django.views.generic import ListView

from main.services.banknote_service import BanknoteService


class BanknoteNewController(ListView):
    """Контроллер для отображения последних 10 банкнот, добавленных в коллекцию.

    Использует BanknoteService для получения данных.
    """

    template_name = "banknotes/new_banknotes.html"
    context_object_name = "banknotes"
    paginate_by = 9
    service = BanknoteService()

    def get_queryset(self) -> list:
        """Возвращает последние 10 банкнот, добавленных в коллекцию."""
        return self.service.get_new_items()
