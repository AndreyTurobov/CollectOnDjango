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
from main.controllers.banknote_controllers.banknote_new_controller import BanknoteNewController
from main.controllers.banknote_controllers.banknote_planned_controller import (
    BanknotePlannedController,
)
from main.controllers.banknote_controllers.banknote_update_controller import (
    BanknoteUpdateController,
)
from main.controllers.choices_controllers.country_create_controller import (
    CountryCreateController,
)
from main.controllers.choices_controllers.country_list_controller import (
    CountryListController,
)
from main.controllers.choices_controllers.material_create_controller import (
    MaterialCreateController,
)
from main.controllers.choices_controllers.state_create_controller import (
    StateCreateController,
)
from main.controllers.choices_controllers.theme_create_controller import (
    ThemeCreateController,
)
from main.controllers.choices_controllers.type_of_edition_create_controller import (
    TypeOfEditionCreateController,
)
from main.controllers.coin_controllers.coin_create_controller import CoinCreateController
from main.controllers.coin_controllers.coin_detail_controller import (
    CoinDetailController,
)
from main.controllers.coin_controllers.coin_list_controller import CoinListController
from main.controllers.coin_controllers.coin_new_controller import CoinNewController
from main.controllers.coin_controllers.coin_planned_controller import CoinPlannedController
from main.controllers.coin_controllers.coin_update_controller import CoinUpdateController
from main.controllers.collection_controllers.collection_create_controller import (
    CollectionCreateController,
)
from main.controllers.collection_controllers.collection_detail_controller import (
    CollectionDetailController,
)
from main.controllers.collection_controllers.collection_list_controller import (
    CollectionListController,
)
from main.controllers.collection_controllers.collection_update_controller import (
    CollectionUpdateController,
)

urlpatterns = [
    path("coins/", CoinListController.as_view(), name="coin-list"),
    path("coins/new/", CoinNewController.as_view(), name="coin-new"),
    path("coins/plan/", CoinPlannedController.as_view(), name="coin-plan"),
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
    path("banknotes/new/", BanknoteNewController.as_view(), name="banknote-new"),
    path("banknotes/plan/", BanknotePlannedController.as_view(), name="banknote-plan"),
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
    path("collections/create/", CollectionCreateController.as_view(), name="create-collection"),
    path("collections/list/", CollectionListController.as_view(), name="collection-list"),
    re_path(
        r"^collections/(?P<slug>[-\w]+)/$",
        CollectionDetailController.as_view(),
        name="collection-detail",
    ),
    re_path(
        r"^collections/(?P<slug>[-\w]+)/update/$",
        CollectionUpdateController.as_view(),
        name="collection-update",
    ),
    path("countries/list/", CountryListController.as_view(), name="country-list"),
    path("create-country/", CountryCreateController.as_view(), name="create-country"),
    path("create-material/", MaterialCreateController.as_view(), name="create-material"),
    path("create-state/", StateCreateController.as_view(), name="create-state"),
    path("create-theme/", ThemeCreateController.as_view(), name="create-theme"),
    path("create-edition/", TypeOfEditionCreateController.as_view(), name="create-edition"),
]
