from django.db import models

from imagekit.models import (
    ImageSpecField,
    ProcessedImageField,
)
from imagekit.processors import ResizeToFill

from main.models.base import CollectorsItem


class CoinModel(CollectorsItem):
    """
    Модель для хранения данных о монетах.

    Наследует общие поля и методы от CollectorsItem.
    """

    edition = models.IntegerField(verbose_name="Тираж")
    weight = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Вес")
    diameter = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Диаметр")
    averse_image = ProcessedImageField(
        upload_to="media/coins_images/",
        default="default_pic/coin-01.jpg",
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 90},
    )
    reverse_image = ProcessedImageField(
        upload_to="media/coins_images/",
        default="default_pic/coin-02.jpg",
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 90},
    )
    averse_thumbnail = ImageSpecField(
        source="averse_image",
        processors=[ResizeToFill(150, 150)],
        format="JPEG",
        options={"quality": 80},
    )
    reverse_thumbnail = ImageSpecField(
        source="reverse_image",
        processors=[ResizeToFill(150, 150)],
        format="JPEG",
        options={"quality": 80},
    )

    def __str__(self):
        return self.full_title

    class Meta:
        """Метаданные модели Coin."""

        db_table = "coins"
        verbose_name = "Монета"
        verbose_name_plural = "Монеты"
