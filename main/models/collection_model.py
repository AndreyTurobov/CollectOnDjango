from django.db import models

from main.models.banknote_model import BanknoteModel
from main.models.base import TimedBaseModel
from main.models.coin_model import CoinModel


class CollectionModel(TimedBaseModel):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(
        max_length=100, allow_unicode=True, unique=True, blank=True, verbose_name="Слаг"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    banknotes = models.ManyToManyField(BanknoteModel, verbose_name="Банкноты", blank=True)
    coins = models.ManyToManyField(CoinModel, verbose_name="Монеты", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        """Мета-класс для модели CollectionModel."""

        db_table = "collections"
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"
