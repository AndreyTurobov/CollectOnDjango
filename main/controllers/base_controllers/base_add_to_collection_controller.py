from main.controllers.base_controllers.base_item_list_controller import BaseItemListController


class BaseAddToCollectionController(BaseItemListController):
    paginate_by = 12

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": self.item_type_title, "url": f"/{self.item_type}/"},
            {"title": "Добавить в коллекцию", "url": ""},
        ]
        return context
