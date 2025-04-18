from django.db import models

from imagekit.models import (
    ImageSpecField,
    ProcessedImageField,
)
from imagekit.processors import ResizeToFill

from main.models.base import CollectorsItem


class BanknoteModel(CollectorsItem):
    """
    Модель для хранения данных о банкнотах.

    Наследует общие поля и методы от CollectorsItem.
    """

    signature = models.CharField(max_length=100, verbose_name="Подпись", default="без подписи")
    size = models.CharField(max_length=50, verbose_name="Размер")
    serial_number = models.CharField(max_length=50, verbose_name="Номер")
    averse_image = ProcessedImageField(
        upload_to="media/notes_images/",
        default="default_pic/note-01.jpg",
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 90},
    )
    reverse_image = ProcessedImageField(
        upload_to="media/notes_images/",
        default="default_pic/note-02.jpg",
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 90},
    )
    averse_thumbnail = ImageSpecField(
        source="averse_image",
        processors=[ResizeToFill(180, 85)],
        format="JPEG",
        options={"quality": 80},
    )
    reverse_thumbnail = ImageSpecField(
        source="reverse_image",
        processors=[ResizeToFill(180, 85)],
        format="JPEG",
        options={"quality": 80},
    )

    @property
    def full_title(self) -> str:
        desc_snippet = (self.description[:64] + " ") if self.description else ""
        return f"{self.country} {self.nominal} {self.currency} {self.year} {desc_snippet}".strip()

    def __str__(self):
        return self.full_title

    class Meta:
        """Метаданные модели Banknote."""

        db_table = "banknotes"
        verbose_name = "Банкнота"
        verbose_name_plural = "Банкноты"
