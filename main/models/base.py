from django.db import models

class TimedBaseModel(models.Model):
    created_at = models.DateTimeField(format='%Y-%m-%d %H:%M:%S', auto_now_add=True)
    updated_at = models.DateTimeField(format='%Y-%m-%d %H:%M:%S', auto_now=True)

    class Meta:
        abstract = True


class CollectorsItem(TimedBaseModel):
    COUNTRY_CHOICES = [
        ('Россия', 'Россия'),
        ('Украина', 'Украина'),
        ('Беларусь', 'Беларусь'),
        ('Казахстан', 'Казахстан'),
        ('Таджикистан', 'Таджикистан'),
        ('Киргизия', 'Киргизия'),
        ('Азербайджан', 'Азербайджан'),
        ('Армения', 'Армения'),
        ('Грузия', 'Грузия'),
        ('Молдова', 'Молдова'),
        ('Туркменистан', 'Туркменистан'),
        ('Узбекистан', 'Узбекистан'),
        ('Латвия', 'Латвия'),
        ('Литва', 'Литва'),
        ('Эстония', 'Эстония'),
        ('Польша', 'Польша'),
        ('Unusual', 'Unusual'),
    ]

    MATERIAL_CHOICES = [
        ('Серебро', 'Серебро'),
        ('Золото', 'Золото'),
        ('Бронза', 'Бронза'),
        ('Никель', 'Никель'),
        ('Медь', 'Медь'),
        ('Латунь', 'Латунь'),
        ('Сталь', 'Сталь'),
        ('Алюминий', 'Алюминий'),
        ('Нейзильбер', 'Нейзильбер'),
        ('Мельхиор', 'Мельхиор'),
        ('Цинковый сплав', 'Цинковый сплав'),
        ('Алюминиевая бронза', 'Алюминиевая бронза'),
        ('Биметалл', 'Биметалл'),
        ('Пластик', 'Пластик'),
        ('Бумага', 'Бумага'),
    ]

    STATE_CHOICES = [
        ('Proof_like', 'Proof_like'),
        ('BUNC', 'Brilliant Uncirculated'),
        ('UNC', 'Uncirculated'),
        ('AUNC', 'About Uncirculated'),
        ('XF', 'Extra Fine'),
        ('VF', 'Very Fine'),
    ]

    TYPE_OF_EDITION_CHOICES = [
        ('Commemorative', 'Commemorative'),
        ('Circulated', 'Circulated'),
        ('Circ/Comm', 'Circulated - Commemorative'),
    ]

    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    nominal = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    km_number = models.CharField(max_length=50, verbose_name="KM#")
    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    full_title = models.CharField(max_length=255, blank=True)
    in_collect = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    type_of_edition = models.CharField(max_length=50, choices=TYPE_OF_EDITION_CHOICES)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.full_title = f"{self.country} {self.nominal} {self.currency} {self.year}"
        super().save(*args, **kwargs)
