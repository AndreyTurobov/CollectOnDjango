from typing import TypeVar

from django.db.models import (
    Count,
    Model,
    Q,
    QuerySet,
)
from django.views.generic import (
    FormView,
    ListView,
)

from main.forms.add_to_collection_form import AddToCollectionForm
from main.models.choice_models import Country, Material, State, Theme, TypeOfEdition
from main.services.banknote_service import BanknoteService
from main.services.coin_service import CoinService
from main.services.collection_service import CollectionService

T = TypeVar("T", bound=Model)


class CoinAddToCollectionListController(ListView):
    """Контроллер для отображения списка монет с возможностью добавления в коллекцию."""

    template_name = "coins/add_to_collection_list.html"
    context_object_name = "coins"
    paginate_by = 12

    def __init__(self, *args, **kwargs):
        """
        Инициализация контроллера.

        Создаёт экземпляр CoinService для работы с данными монет.
        """
        super().__init__(*args, **kwargs)
        self.service = CoinService()

    def _get_annotated_models(self, model_class: type[Model]) -> QuerySet:
        """Возвращает модели с аннотацией item_count."""
        return model_class.objects.annotate(item_count=Count("coinmodel")).filter(item_count__gt=0)

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
            {"title": "Монеты", "url": "/coins/"},
            {"title": "Добавить в коллекцию", "url": ""},
        ]
        return context

    def get_queryset(self) -> QuerySet[T]:
        """Возвращает отфильтрованный список монет на основе параметров запроса."""
        name_filter = self.request.GET.get("name", "")
        filters = {
            "country__id": self.request.GET.get("country"),
            "year": self.request.GET.get("year", ""),
            "km_number": self.request.GET.get("km_number", ""),
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


class BanknoteAddToCollectionListController(ListView):
    """Контроллер для отображения списка банкнот с возможностью добавления в коллекцию."""

    template_name = "banknotes/add_to_collection_list.html"
    context_object_name = "banknotes"
    paginate_by = 12

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
            {"title": "Банкноты", "url": "/banknotes/"},
            {"title": "Добавить в коллекцию", "url": ""},
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


class AddItemToCollectionFormController(FormView):
    """Контроллер для обработки формы добавления предмета (монеты/банкноты) в коллекцию."""

    service = CollectionService
    template_name = "collections/add_to_collection_form.html"
    form_class = AddToCollectionForm
    success_url = "/collections/list/"

    def get_form_kwargs(self) -> dict:
        """Добавляет список коллекций в kwargs для формы."""
        kwargs = super().get_form_kwargs()
        kwargs["collections"] = self.service().get_all()
        return kwargs

    def form_valid(self, form) -> str:
        """Обрабатывает валидную форму, добавляя предмет в выбранную коллекцию."""
        collection_slug = form.cleaned_data["collection"]
        item_type = self.kwargs["item_type"]
        item_slug = self.kwargs["item_slug"]

        service = self.service()
        match item_type:
            case "coin":
                service.add_coin_to_collection(collection_slug, item_slug)
            case "banknote":
                service.add_banknote_to_collection(collection_slug, item_slug)

        return super().form_valid(form)
