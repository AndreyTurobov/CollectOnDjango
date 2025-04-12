from typing import (
    Generic,
    TypeVar,
)

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

T = TypeVar("T", bound=Model)
M = TypeVar("M", bound=Model)  # Модель для аннотации (CoinModel/BanknoteModel)


class BaseItemListController(ListView, Generic[T, M]):
    """
    Базовый контроллер для отображения списка предметов (монет/банкнот).

    Реализует общую логику для фильтрации, пагинации и отображения.
    """

    paginate_by = 9
    item_service = None  # Определяется в дочерних классах
    filter_fields = {
        "country__id": "country",
        "year": "year",
        "km_number": "km_number",
        "material__id": "material",
        "state__id": "state",
        "themes__id": "themes_id",
        "type_of_edition__id": "type_of_edition",
    }
    search_fields = [
        "country__title__icontains",
        "nominal__icontains",
        "currency__icontains",
        "year__icontains",
        "description__icontains",
    ]
    annotated_model_relation = None  # Например: "coinmodel" или "banknotemodel"

    def _get_annotated_models(self, model_class: type[Model]) -> QuerySet:
        """Оптимизированный метод для получения моделей с аннотацией количества."""
        return (
            model_class.objects.annotate(item_count=Count(self.annotated_model_relation))
            .filter(item_count__gt=0)
            .select_related()
            .order_by("title")
        )

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.object_list = self.get_queryset()

    def get_context_data(self, **kwargs) -> dict:
        """Общий контекст для всех списков предметов."""
        context = super().get_context_data(**kwargs)
        context["countries"] = self._get_annotated_models(Country)
        context["materials"] = self._get_annotated_models(Material)
        context["states"] = self._get_annotated_models(State)
        context["themes"] = self._get_annotated_models(Theme)
        context["type_of_editions"] = self._get_annotated_models(TypeOfEdition)
        return context

    def _apply_filters(self, queryset: QuerySet[T]) -> QuerySet[T]:
        """Применяет фильтры из GET-параметров."""
        filters = {
            field: self.request.GET.get(param)
            for field, param in self.filter_fields.items()
            if self.request.GET.get(param)
        }
        return queryset.filter(**filters)

    def _apply_search(self, queryset: QuerySet[T]) -> QuerySet[T]:
        """Применяет поиск по тексту."""
        if search_term := self.request.GET.get("name", ""):
            query = Q()
            for field in self.search_fields:
                query |= Q(**{field: search_term})
            return queryset.filter(query)
        return queryset

    def get_queryset(self) -> QuerySet[T]:
        """Возвращает оптимизированный QuerySet с фильтрацией."""
        queryset = self.item_service.get_all()
        queryset = self._apply_filters(queryset)
        queryset = self._apply_search(queryset)
        return queryset.order_by("id")
