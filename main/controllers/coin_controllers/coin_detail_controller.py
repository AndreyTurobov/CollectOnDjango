from django.views.generic import DetailView

from main.services.coin_service import CoinService


class CoinDetailController(DetailView):
    """
    Контроллер для отображения детальной информации о монете.

    Использует шаблон 'coins/detail_coin.html' и передаёт в контекст объект 'coin'.
    """

    template_name = "coins/detail_coin.html"
    context_object_name = "coin"

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр CoinService для работы с данными монет.
        """
        super().__init__(*args, **kwargs)
        self.service = CoinService()

    def get_object(self, queryset=None):
        """Возвращает объект монеты по его slug."""
        return self.service.get_by_slug(self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        coin = self.get_object()
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Монеты", "url": "/coins/"},
            {"title": coin.full_title, "url": ""},
        ]
        return context
