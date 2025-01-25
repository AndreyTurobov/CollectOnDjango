from django.urls import path

from .views.coin_views import (
    CoinListView,
    CoinDetailView,
)
from .views.banknote_views import (
    BanknoteListView,
    BanknoteDetailView,
)


urlpatterns = [
    path('coins/', CoinListView.as_view(), name='coin-list'),
    path('coins/<int:pk>/', CoinDetailView.as_view(), name='coin-detail'),
    path('banknotes/', BanknoteListView.as_view(), name='banknote-list'),
    path('banknotes/<int:pk>/', BanknoteDetailView.as_view(), name='banknote-detail'),
]
