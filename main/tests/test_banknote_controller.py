import pytest

from main.controllers.banknote_controllers.banknote_list_controller import BanknoteListController


class TestBanknoteListController:
    @pytest.mark.django_db
    def test_get_context_data(self, rf, banknote):
        request = rf.get("/")
        controller = BanknoteListController()
        controller.setup(request)  # Инициализируем контроллер

        context = controller.get_context_data()

        assert "countries" in context
        assert "breadcrumbs" in context
        assert context["breadcrumbs"][1]["title"] == "Банкноты"
        assert banknote in controller.object_list  # Проверяем что объект в списке

    @pytest.mark.django_db
    def test_get_queryset(self, rf, banknote):
        request = rf.get(f"/?country={banknote.country.id}")
        controller = BanknoteListController()
        controller.setup(request)

        qs = controller.get_queryset()
        assert qs.count() == 1
        assert qs[0].nominal == "10"
