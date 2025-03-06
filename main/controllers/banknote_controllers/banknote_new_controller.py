from django.db.models import QuerySet

from main.controllers.banknote_controllers.banknote_list_controller import BanknoteListController


class BanknoteNewController(BanknoteListController):
    """Контроллер для отображения монет которые планируется добавить в коллекцию.

    Использует CoinService для получения данных.
    """

    template_name = "banknotes/new_banknotes.html"

    def get_queryset(self) -> QuerySet:
        """Возвращает QuerySet монет, которые планируются добавить в коллекцию."""
        qs = self.service.get_new_items()
        return qs

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Новые банкноты"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Банкноты", "url": "/banknotes/"},
            {"title": "Новые банкноты", "url": ""},
        ]
        return context
