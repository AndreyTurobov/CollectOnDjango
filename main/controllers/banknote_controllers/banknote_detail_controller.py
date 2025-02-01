from django.views.generic import DetailView

from main.services.banknote_service import BanknoteService


class BanknoteDetailController(DetailView):
    """
    Контроллер для отображения детальной информации о банкноте.

    Использует шаблон 'banknotes/detail.html' и передаёт в контекст объект 'banknote'.
    """

    template_name = "banknotes/detail.html"
    context_object_name = "banknote"

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр BanknoteService для работы с данными банкнот.
        """
        super().__init__(*args, **kwargs)
        self.service = BanknoteService()

    def get_object(self, queryset=None):
        """Возвращает объект банкноты по его ID."""
        return self.service.get_by_slug(self.kwargs["slug"])
