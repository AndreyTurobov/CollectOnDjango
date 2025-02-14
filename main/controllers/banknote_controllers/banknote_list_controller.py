from django.db.models import Count
from django.views.generic import ListView

from main.models.choice_models import (
    Country,
    Material,
    State,
    TypeOfEdition,
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
        """Добавляет choice_models в контекст шаблона для использования в фильтрах."""
        context = super().get_context_data(**kwargs)
        context["countries"] = Country.objects.annotate(item_count=Count("banknotemodel")).filter(
            item_count__gt=0
        )
        context["materials"] = Material.objects.annotate(item_count=Count("banknotemodel")).filter(
            item_count__gt=0
        )
        context["states"] = State.objects.annotate(item_count=Count("banknotemodel")).filter(
            item_count__gt=0
        )
        context["type_of_editions"] = TypeOfEdition.objects.annotate(
            item_count=Count("banknotemodel")
        ).filter(item_count__gt=0)
        return context

    def get_queryset(self):
        """Возвращает отфильтрованный список банкнот на основе параметров запроса."""
        filters = {
            "full_title__icontains": self.request.GET.get("name", ""),
            "country__id": self.request.GET.get("country"),
            "year": self.request.GET.get("year", ""),
            "km_number": self.request.GET.get("km_number", ""),
            "material__id": self.request.GET.get("material"),
            "state__id": self.request.GET.get("state"),
            "type_of_edition__id": self.request.GET.get("type_of_edition"),
        }

        return self.service.get_by_filter(filters).order_by("id")
