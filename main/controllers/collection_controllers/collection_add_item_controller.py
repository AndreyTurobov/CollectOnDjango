from django.db.models import QuerySet
from django.views.generic import (
    FormView,
    ListView,
)

from main.forms.add_to_collection_form import AddToCollectionForm
from main.services.banknote_service import BanknoteService
from main.services.coin_service import CoinService
from main.services.collection_service import CollectionService


class CoinAddToCollectionListController(ListView):
    service = CoinService
    template_name = "coins/add_to_collection_list.html"
    context_object_name = "coins"
    paginate_by = 12

    def get_queryset(self) -> QuerySet[CoinService]:
        return self.service().get_all()


class BanknoteAddToCollectionListController(ListView):
    service = BanknoteService
    template_name = "banknotes/add_to_collection_list.html"
    context_object_name = "banknotes"
    paginate_by = 12

    def get_queryset(self) -> QuerySet[BanknoteService]:
        return self.service().get_all()


class AddItemToCollectionFormController(FormView):
    service = CollectionService
    template_name = "collections/add_to_collection_form.html"
    form_class = AddToCollectionForm
    success_url = "/collections/list/"

    def get_form_kwargs(self) -> dict:
        kwargs = super().get_form_kwargs()
        kwargs["collections"] = self.service().get_all()
        return kwargs

    def form_valid(self, form) -> str:
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
