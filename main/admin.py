from django.contrib import admin

from main.models.banknote_model import BanknoteModel
from main.models.choice_models import (
    Country,
    Material,
    State,
    Theme,
    TypeOfEdition,
)
from main.models.coin_model import CoinModel
from main.models.collection_model import (
    CollectionBanknoteModel,
    CollectionCoinModel,
    CollectionModel,
)


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
    filter_horizontal = ("themes",)


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
    filter_horizontal = ("themes",)


class CollectionBanknoteInline(admin.TabularInline):
    model = CollectionBanknoteModel
    extra = 0


class CollectionCoinInline(admin.TabularInline):
    model = CollectionCoinModel
    extra = 0


@admin.register(CollectionModel)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    inlines = [CollectionBanknoteInline, CollectionCoinInline]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeOfEdition)
class TypeOfEditionAdmin(admin.ModelAdmin):
    pass
