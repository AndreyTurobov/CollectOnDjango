from typing import TypeVar

from django.db.models import Model
from django.views.generic import FormView

from main.controllers.base_controllers.base_add_to_collection_controller import (
    BaseAddToCollectionController,
)
from main.forms.add_to_collection_form import AddToCollectionForm
from main.services.banknote_service import BanknoteService
from main.services.coin_service import CoinService
from main.services.collection_service import CollectionService

T = TypeVar("T", bound=Model)


class CoinAddToCollectionListController(BaseAddToCollectionController):
    template_name = "coins/add_to_collection_list.html"
    context_object_name = "coins"
    item_service = CoinService()
    annotated_model_relation = "coinmodel"
    item_type = "coins"
    item_type_title = "Монеты"


class BanknoteAddToCollectionListController(BaseAddToCollectionController):
    template_name = "banknotes/add_to_collection_list.html"
    context_object_name = "banknotes"
    item_service = BanknoteService()
    annotated_model_relation = "banknotemodel"
    item_type = "banknotes"
    item_type_title = "Банкноты"


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
