import pytest

from main.controllers.collection_controllers.collection_add_item_controller import (
    CoinAddToCollectionListController,
)


class TestCoinAddToCollectionListController:
    @pytest.mark.django_db
    def test_context_breadcrumbs(self, rf, coin):
        len_context = 3
        request = rf.get("/")
        controller = CoinAddToCollectionListController()
        controller.setup(request)  # Инициализация

        context = controller.get_context_data()

        assert len(context["breadcrumbs"]) == len_context
        assert context["breadcrumbs"][1]["title"] == "Монеты"
        assert context["breadcrumbs"][2]["title"] == "Добавить в коллекцию"

    @pytest.mark.django_db
    def test_pagination(self, rf, coin):
        pagination_size = 12
        request = rf.get("/")
        controller = CoinAddToCollectionListController()
        controller.setup(request)

        assert controller.paginate_by == pagination_size
        assert controller.object_list.count() == 1
