from django.contrib import admin
from .models.coin import Coin
from .models.banknote import Banknote


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('full_title', 'country', 'year', 'material', 'weight', 'diameter')
    search_fields = ('full_title', 'country', 'year')


@admin.register(Banknote)
class BanknoteAdmin(admin.ModelAdmin):
    list_display = ('full_title', 'country', 'year', 'signature', 'size', 'serial_number')
    search_fields = ('full_title', 'country', 'year')
