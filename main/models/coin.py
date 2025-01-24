from django.db import models
from .base import CollectorsItem


class Coin(CollectorsItem):
    edition = models.IntegerField()
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    diameter = models.DecimalField(max_digits=4, decimal_places=2)
    averse_image = models.ImageField(upload_to='media/coins_images/', default='default_pic/coin-01.jpg')
    reverse_image = models.ImageField(upload_to='media/coins_images/', default='default_pic/coin-02.jpg')

    def __str__(self):
        return self.full_title
