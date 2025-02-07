from django.urls import path

from main.controllers.banknote_controllers.banknote_create_controller import (
    BanknoteCreateController,
)
from main.controllers.banknote_controllers.banknote_detail_controller import (
    BanknoteDetailController,
)
from main.controllers.banknote_controllers.banknote_list_controller import (
    BanknoteListController,
)
from main.controllers.coin_controllers.coin_create_controller import CoinCreateController
from main.controllers.coin_controllers.coin_detail_controller import (
    CoinDetailController,
)
from main.controllers.coin_controllers.coin_list_controller import CoinListController

urlpatterns = [
    path("coins/", CoinListController.as_view(), name="coin-list"),
    path("coins/create/", CoinCreateController.as_view(), name="create-coin"),
    path("coins/<slug:slug>/", CoinDetailController.as_view(), name="coin-detail"),
    path("banknotes/", BanknoteListController.as_view(), name="banknote-list"),
    path("banknotes/create/", BanknoteCreateController.as_view(), name="create-banknote"),
    path("banknotes/<slug:slug>/", BanknoteDetailController.as_view(), name="banknote-detail"),
]
