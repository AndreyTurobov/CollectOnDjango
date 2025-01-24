from django.urls import path
from .views.coin_views import CoinListView
from .views.banknote_views import BanknoteListView


urlpatterns = [
    path('coins/', CoinListView.as_view(), name='coin-list'),
    path('banknotes/', BanknoteListView.as_view(), name='banknote-list'),
]
