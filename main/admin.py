from django.contrib import admin

from main.models.banknote_model import BanknoteModel
from main.models.choice_models import (
    Country,
    Material,
    State,
    TypeOfEdition,
)
from main.models.coin_model import CoinModel


@admin.register(CoinModel)
class CoinAdmin(admin.ModelAdmin):
    list_display = (
        "full_title",
        "country",
        "year",
        "material",
        "weight",
        "diameter",
    )
    search_fields = (
        "full_title",
        "country",
        "year",
    )


@admin.register(BanknoteModel)
class BanknoteAdmin(admin.ModelAdmin):
    list_display = (
        "full_title",
        "country",
        "year",
        "signature",
        "size",
        "serial_number",
    )
    search_fields = (
        "full_title",
        "country",
        "year",
    )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeOfEdition)
class TypeOfEditionAdmin(admin.ModelAdmin):
    pass
