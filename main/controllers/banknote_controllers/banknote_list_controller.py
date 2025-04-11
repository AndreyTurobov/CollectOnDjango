from main.controllers.base_controllers.base_item_list_controller import BaseItemListController
from main.services.banknote_service import BanknoteService


class BanknoteListController(BaseItemListController):
    template_name = "banknotes/list_banknotes.html"
    context_object_name = "banknotes"
    item_service = BanknoteService()
    annotated_model_relation = "banknotemodel"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Банкноты", "url": ""},
        ]
        return context
