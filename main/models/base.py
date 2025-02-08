from django.db import models
from django.utils.text import slugify

from main.models.slug_generator import generate_unique_slug


class TimedBaseModel(models.Model):
    """Абстрактная модель для хранения общих данных об объектах моделей."""

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        """Метаданные абстрактной модели TimedBaseModel."""

        abstract = True


class CollectorsItem(TimedBaseModel):
    """Абстрактная модель для хранения общих данных о коллекционных предметах."""

    COUNTRY_CHOICES = [
        ("Россия", "Россия"),
        ("Украина", "Украина"),
        ("Беларусь", "Беларусь"),
        ("Казахстан", "Казахстан"),
        ("Таджикистан", "Таджикистан"),
        ("Киргизия", "Киргизия"),
        ("Азербайджан", "Азербайджан"),
        ("Армения", "Армения"),
        ("Грузия", "Грузия"),
        ("Молдова", "Молдова"),
        ("Туркменистан", "Туркменистан"),
        ("Узбекистан", "Узбекистан"),
        ("Латвия", "Латвия"),
        ("Литва", "Литва"),
        ("Эстония", "Эстония"),
        ("Польша", "Польша"),
        ("Unusual", "Unusual"),
    ]

    MATERIAL_CHOICES = [
        ("Серебро", "Серебро"),
        ("Золото", "Золото"),
        ("Бронза", "Бронза"),
        ("Никель", "Никель"),
        ("Медь", "Медь"),
        ("Латунь", "Латунь"),
        ("Сталь", "Сталь"),
        ("Алюминий", "Алюминий"),
        ("Нейзильбер", "Нейзильбер"),
        ("Мельхиор", "Мельхиор"),
        ("Цинковый сплав", "Цинковый сплав"),
        ("Алюминиевая бронза", "Алюминиевая бронза"),
        ("Биметалл", "Биметалл"),
        ("Пластик", "Пластик"),
        ("Бумага", "Бумага"),
    ]

    STATE_CHOICES = [
        ("Proof_like", "Proof_like"),
        ("BUNC", "Brilliant Uncirculated"),
        ("UNC", "Uncirculated"),
        ("AUNC", "About Uncirculated"),
        ("XF", "Extra Fine"),
        ("VF", "Very Fine"),
    ]

    TYPE_OF_EDITION_CHOICES = [
        ("Commemorative", "Commemorative"),
        ("Circulated", "Circulated"),
        ("Circ/Comm", "Circulated - Commemorative"),
    ]

    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, verbose_name="Страна")
    nominal = models.CharField(max_length=50, verbose_name="Номинал")
    currency = models.CharField(max_length=50, verbose_name="Валюта")
    year = models.CharField(max_length=4, verbose_name="Год выпуска")
    km_number = models.CharField(max_length=50, verbose_name="KM#")
    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES, verbose_name="Материал")
    state = models.CharField(max_length=50, choices=STATE_CHOICES, verbose_name="Состояние")
    in_collect = models.BooleanField(default=False, verbose_name="В коллекции")
    description = models.TextField(blank=True, verbose_name="Описание")
    slug = models.SlugField(
        max_length=255, allow_unicode=True, unique=True, blank=True, verbose_name="Слаг"
    )
    type_of_edition = models.CharField(
        max_length=50, choices=TYPE_OF_EDITION_CHOICES, verbose_name="Тип выпуска"
    )

    class Meta:
        """Метаданные абстрактной модели CollectorsItem."""

        abstract = True

    @property
    def full_title(self) -> str:
        raise NotImplementedError("Дочерние классы должны реализовать это свойство")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.full_title, allow_unicode=True)
            base_slug = base_slug[:255].strip("-")
            self.slug = generate_unique_slug(self.__class__, base_slug)
        super().save(*args, **kwargs)
