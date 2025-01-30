from django.urls import path

from main.controllers.coin_controllers.coin_detail_controller import CoinDetailController
from main.controllers.coin_controllers.coin_list_controller import CoinListController
from main.controllers.banknote_controllers.banknote_detail_controller import BanknoteDetailController
from main.controllers.banknote_controllers.banknote_list_controller import BanknoteListController

urlpatterns = [
    path('coins/', CoinListController.as_view(), name='coin-list'),
    path('coins/<int:pk>/', CoinDetailController.as_view(), name='coin-detail'),
    path('banknotes/', BanknoteListController.as_view(), name='banknote-list'),
    path('banknotes/<int:pk>/', BanknoteDetailController.as_view(), name='banknote-detail'),
]
