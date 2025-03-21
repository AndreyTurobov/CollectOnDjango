from typing import TypeVar

from django.db.models import (
    Count,
    Model,
    Q,
    QuerySet,
)
from django.views.generic import ListView

from main.models.choice_models import (
    Country,
    Material,
    State,
    Theme,
    TypeOfEdition,
)
from main.services.banknote_service import BanknoteService

# Определяем типовую переменную для модели
T = TypeVar("T", bound=Model)


class BanknoteListController(ListView):
    """
    Контроллер для отображения списка банкнот.

    Использует шаблон 'banknotes/list_banknotes.html' и передаёт в контекст объекты 'banknotes'.
    Поддерживает пагинацию (по 9 элементов на странице).
    """

    template_name = "banknotes/list_banknotes.html"
    context_object_name = "banknotes"
    paginate_by = 9

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр BanknoteService для работы с данными банкнот.
        """
        super().__init__(*args, **kwargs)
        self.service = BanknoteService()

    def _get_annotated_models(self, model_class: type[Model]) -> QuerySet:
        """Возвращает модели с аннотацией item_count."""
        return model_class.objects.annotate(item_count=Count("banknotemodel")).filter(
            item_count__gt=0
        )

    def get_context_data(self, **kwargs) -> dict:
        """Добавляет choice_models в контекст шаблона для использования в фильтрах."""
        context = super().get_context_data(**kwargs)
        context["countries"] = self._get_annotated_models(Country)
        context["materials"] = self._get_annotated_models(Material)
        context["states"] = self._get_annotated_models(State)
        context["themes"] = self._get_annotated_models(Theme)
        context["type_of_editions"] = self._get_annotated_models(TypeOfEdition)
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Банкноты", "url": ""},
        ]
        return context

    def get_queryset(self) -> QuerySet[T]:
        """Возвращает отфильтрованный список банкнот на основе параметров запроса."""
        name_filter = self.request.GET.get("name", "")
        filters = {
            "country__id": self.request.GET.get("country"),
            "year": self.request.GET.get("year", ""),
            "km_number": self.request.GET.get("km_number"),
            "material__id": self.request.GET.get("material"),
            "state__id": self.request.GET.get("state"),
            "themes__id": self.request.GET.get("themes__id"),
            "type_of_edition__id": self.request.GET.get("type_of_edition"),
        }

        queryset: QuerySet[T] = self.service.get_by_filter(filters)

        if name_filter:
            queryset = queryset.filter(
                Q(country__title__icontains=name_filter)
                | Q(nominal__icontains=name_filter)
                | Q(currency__icontains=name_filter)
                | Q(year__icontains=name_filter)
                | Q(description__icontains=name_filter)
            )

        return queryset.order_by("id")
