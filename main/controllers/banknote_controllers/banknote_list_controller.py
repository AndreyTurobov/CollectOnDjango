from django.views.generic import ListView

from main.models.choices import (
    COUNTRY_CHOICES,
    MATERIAL_CHOICES,
    STATE_CHOICES,
    TYPE_OF_EDITION_CHOICES,
)
from main.services.banknote_service import BanknoteService


class BanknoteListController(ListView):
    """
    Контроллер для отображения списка банкнот.

    Использует шаблон 'banknotes/list.html' и передаёт в контекст объекты 'banknotes'.
    Поддерживает пагинацию (по 9 элементов на странице).
    """

    template_name = "banknotes/list.html"
    context_object_name = "banknotes"
    paginate_by = 9

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр BanknoteService для работы с данными банкнот.
        """
        super().__init__(*args, **kwargs)
        self.service = BanknoteService()

    def get_context_data(self, **kwargs):
        """Добавляет CHOICES в контекст шаблона для использования в фильтрах."""
        context = super().get_context_data(**kwargs)
        context["COUNTRY_CHOICES"] = COUNTRY_CHOICES
        context["MATERIAL_CHOICES"] = MATERIAL_CHOICES
        context["STATE_CHOICES"] = STATE_CHOICES
        context["TYPE_OF_EDITION_CHOICES"] = TYPE_OF_EDITION_CHOICES
        return context

    def get_queryset(self):
        """Возвращает отфильтрованный список банкнот на основе параметров запроса."""
        filters = {
            "full_title__icontains": self.request.GET.get("name", ""),
            "country": self.request.GET.get("country", ""),
            "year": self.request.GET.get("year", ""),
            "km_number": self.request.GET.get("km_number", ""),
            "material": self.request.GET.get("material", ""),
            "state": self.request.GET.get("state", ""),
            "type_of_edition": self.request.GET.get("type_of_edition", ""),
        }

        return self.service.get_by_filter(filters).order_by("id")
