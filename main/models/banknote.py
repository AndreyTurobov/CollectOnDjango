from django.db import models
from .base import CollectorsItem


class Banknote(CollectorsItem):
    signature = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    averse_image = models.ImageField(upload_to='media/notes_images/', default='default_pic/note-01.jpg')
    reverse_image = models.ImageField(upload_to='media/notes_images/', default='default_pic/note-02.jpg')

    def __str__(self):
        return self.full_title
