from django.db import models
from imagekit.models import (
    ProcessedImageField,
    ImageSpecField,
)
from imagekit.processors import ResizeToFill
from .base import CollectorsItem


class Coin(CollectorsItem):
    edition = models.IntegerField()
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    diameter = models.DecimalField(max_digits=4, decimal_places=2)
    averse_image = ProcessedImageField(
        upload_to='media/coins_images/',
        default='default_pic/coin-01.jpg',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 90}
    )
    reverse_image = ProcessedImageField(
        upload_to='media/coins_images/',
        default='default_pic/coin-02.jpg',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 90}
    )
    averse_thumbnail = ImageSpecField(
        source='averse_image',
        processors=[ResizeToFill(150, 150)],
        format='JPEG',
        options={'quality': 80}
    )
    reverse_thumbnail = ImageSpecField(
        source='reverse_image',
        processors=[ResizeToFill(150, 150)],
        format='JPEG',
        options={'quality': 80}
    )

    def __str__(self):
        return self.full_title
