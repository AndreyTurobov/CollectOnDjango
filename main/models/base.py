from django.db import models
from django.utils.text import slugify

from main.models.choice_models import (
    Country,
    Material,
    State,
    TypeOfEdition,
)
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

    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name="Страна")
    nominal = models.CharField(max_length=50, verbose_name="Номинал")
    currency = models.CharField(max_length=50, verbose_name="Валюта")
    year = models.CharField(max_length=4, verbose_name="Год выпуска")
    km_number = models.CharField(max_length=50, verbose_name="KM#")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Материал")
    state = models.ForeignKey(State, on_delete=models.PROTECT, verbose_name="Состояние")
    in_collect = models.BooleanField(default=False, verbose_name="В коллекции")
    description = models.TextField(blank=True, verbose_name="Описание")
    slug = models.SlugField(
        max_length=255, allow_unicode=True, unique=True, blank=True, verbose_name="Слаг"
    )
    type_of_edition = models.ForeignKey(
        TypeOfEdition, on_delete=models.PROTECT, verbose_name="Тип выпуска"
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
