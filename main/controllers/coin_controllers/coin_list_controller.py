from main.controllers.base_controllers.base_item_list_controller import BaseItemListController
from main.services.coin_service import CoinService


class CoinListController(BaseItemListController):
    template_name = "coins/list_coins.html"
    context_object_name = "coins"
    item_service = CoinService()
    annotated_model_relation = "coinmodel"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Монеты", "url": ""},
        ]
        return context
