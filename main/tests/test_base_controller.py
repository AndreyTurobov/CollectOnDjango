import pytest

from main.controllers.base_controllers.base_item_list_controller import BaseItemListController
from main.models.banknote_model import BanknoteModel
from main.models.choice_models import Country
from main.services.banknote_service import BanknoteService


class TestBaseItemListController:
    @pytest.mark.django_db
    def test_get_annotated_models(self, country, banknote):
        controller = BaseItemListController()
        controller.annotated_model_relation = "banknotemodel"

        countries = controller._get_annotated_models(Country)
        assert countries.count() == 1
        assert countries[0].item_count == 1

    @pytest.mark.django_db
    def test_apply_filters(self, rf, banknote):
        request = rf.get("/?country=1&year=2020")
        controller = BaseItemListController()
        controller.request = request
        controller.item_service = BanknoteService()
        controller.filter_fields = {"country__id": "country", "year": "year"}

        qs = BanknoteModel.objects.all()
        filtered_qs = controller._apply_filters(qs)

        assert filtered_qs.count() == 1
        assert filtered_qs[0].km_number == "123"

    @pytest.mark.django_db
    def test_apply_search(self, rf, banknote):
        request = rf.get("/?name=Test")
        controller = BaseItemListController()
        controller.request = request
        controller.search_fields = ["country__title__icontains"]

        qs = BanknoteModel.objects.all()
        searched_qs = controller._apply_search(qs)

        assert searched_qs.count() == 1
