from django.views.generic import DetailView

from main.services.coin_service import CoinService


class CoinDetailController(DetailView):
    """
    Контроллер для отображения детальной информации о монете.

    Использует шаблон 'coins/detail.html' и передаёт в контекст объект 'coin'.
    """

    template_name = "coins/detail.html"
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
