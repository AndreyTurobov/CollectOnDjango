from django.urls import (
    path,
    re_path,
)

from main.controllers.banknote_controllers.banknote_create_controller import (
    BanknoteCreateController,
)
from main.controllers.banknote_controllers.banknote_detail_controller import (
    BanknoteDetailController,
)
from main.controllers.banknote_controllers.banknote_list_controller import (
    BanknoteListController,
)
from main.controllers.banknote_controllers.banknote_update_controller import (
    BanknoteUpdateController,
)
from main.controllers.choices_controllers.country_list_controller import CountryListView
from main.controllers.coin_controllers.coin_create_controller import CoinCreateController
from main.controllers.coin_controllers.coin_detail_controller import (
    CoinDetailController,
)
from main.controllers.coin_controllers.coin_list_controller import CoinListController
from main.controllers.coin_controllers.coin_update_controller import CoinUpdateController

urlpatterns = [
    path("coins/", CoinListController.as_view(), name="coin-list"),
    path("coins/create/", CoinCreateController.as_view(), name="create-coin"),
    re_path(
        r"^coins/(?P<slug>[-\w]+)/$",
        CoinDetailController.as_view(),
        name="coin-detail",
    ),
    re_path(
        r"^coins/(?P<slug>[-\w]+)/update/$",
        CoinUpdateController.as_view(),
        name="coin-update",
    ),
    path("banknotes/", BanknoteListController.as_view(), name="banknote-list"),
    path("banknotes/create/", BanknoteCreateController.as_view(), name="create-banknote"),
    re_path(
        r"^banknotes/(?P<slug>[-\w]+)/$",
        BanknoteDetailController.as_view(),
        name="banknote-detail",
    ),
    re_path(
        r"^banknotes/(?P<slug>[-\w]+)/update/$",
        BanknoteUpdateController.as_view(),
        name="banknote-update",
    ),
    path("countries/list/", CountryListView.as_view(), name="country-list"),
]
