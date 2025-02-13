from django.db import models


class Country(models.Model):
    """Модель страна происхождения коллекционного объекта Country."""

    title = models.CharField(max_length=50, unique=True, verbose_name="Страна")

    def __str__(self):
        return self.title

    class Meta:
        """Метаданные модели Country."""

        db_table = "countries"
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Material(models.Model):
    """Модель материал коллекционного объекта Material."""

    title = models.CharField(max_length=50, unique=True, verbose_name="Материал")

    def __str__(self):
        return self.title

    class Meta:
        """Метаданные модели Material."""

        db_table = "materials"
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class State(models.Model):
    """Модель состояния коллекционного объекта State."""

    title = models.CharField(max_length=50, unique=True, verbose_name="Состояние")

    def __str__(self):
        return self.title

    class Meta:
        """Метаданные модели State."""

        db_table = "states"
        verbose_name = "Состояние"
        verbose_name_plural = "Состояния"


class TypeOfEdition(models.Model):
    """Модель типа издания коллекционного объекта TypeOfEdition."""

    title = models.CharField(max_length=50, unique=True, verbose_name="Тип выпуска")

    def __str__(self):
        return self.title

    class Meta:
        """Метаданные модели TypeOfEdition."""

        db_table = "type_of_editions"
        verbose_name = "Тип выпуска"
        verbose_name_plural = "Типы выпуска"
