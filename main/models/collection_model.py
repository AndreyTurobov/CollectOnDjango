from django.db import models

from main.models.banknote_model import BanknoteModel
from main.models.base import TimedBaseModel
from main.models.coin_model import CoinModel


class CollectionBanknoteModel(models.Model):
    """Промежуточная модель для связи коллекций и банкнот."""

    collection = models.ForeignKey("CollectionModel", on_delete=models.CASCADE)
    banknote = models.ForeignKey(BanknoteModel, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)


class CollectionCoinModel(models.Model):
    """Промежуточная модель для связи коллекций и монет."""

    collection = models.ForeignKey("CollectionModel", on_delete=models.CASCADE)
    coin = models.ForeignKey(CoinModel, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)


class CollectionModel(TimedBaseModel):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(
        max_length=100, allow_unicode=True, unique=True, blank=True, verbose_name="Слаг"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    banknotes = models.ManyToManyField(
        BanknoteModel, through="CollectionBanknoteModel", verbose_name="Банкноты", blank=True
    )
    coins = models.ManyToManyField(
        CoinModel, through="CollectionCoinModel", verbose_name="Монеты", blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        """Мета-класс для модели CollectionModel."""

        db_table = "collections"
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"
