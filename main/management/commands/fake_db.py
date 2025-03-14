from django.core.management.base import BaseCommand

from faker import Faker

from main.models.banknote_model import BanknoteModel
from main.models.choice_models import (
    Country,
    Material,
    State,
    Theme,
    TypeOfEdition,
)
from main.models.coin_model import CoinModel


class Command(BaseCommand):
    help = "Заполняет базу данных фейковыми данными для моделей Coin и Banknote."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, default=10, help="Количество записей для каждой модели."
        )

    def handle(self, *args, **options):
        fake = Faker()
        count = options["count"]

        # 1. Создание всех связанных объектов и их явное сохранение
        countries = []
        for title in [
            "Россия",
            "Украина",
            "Беларусь",
            "Казахстан",
            "Таджикистан",
            "Киргизия",
            "Азербайджан",
            "Армения",
            "Грузия",
            "Молдова",
            "Туркменистан",
            "Узбекистан",
            "Латвия",
            "Литва",
            "Эстония",
            "Польша",
        ]:
            country, _ = Country.objects.get_or_create(
                title=title, defaults={"flag": f"flags/{title}.jpg"}
            )
            countries.append(country)

        materials = [
            Material.objects.get_or_create(title=title)[0]
            for title in [
                "Серебро",
                "Золото",
                "Бронза",
                "Никель",
                "Медь",
                "Латунь",
                "Сталь",
                "Алюминий",
                "Нейзильбер",
                "Мельхиор",
                "Цинковый сплав",
                "Алюминиевая бронза",
                "Биметалл",
                "Пластик",
                "Бумага",
            ]
        ]

        states = [
            State.objects.get_or_create(title=title)[0]
            for title in [
                "ProofLike",
                "BrilliantUncirculated",
                "Uncirculated",
                "AboutUncirculated",
                "ExtraFine",
                "VeryFine",
            ]
        ]

        themes = [
            Theme.objects.get_or_create(title=title)[0]
            for title in [
                "Люди",
                "События",
                "Флора",
                "Фауна",
                "Культура",
            ]
        ]

        types_of_edition = [
            TypeOfEdition.objects.get_or_create(title=title)[0]
            for title in ["Commemorative", "Circulated", "Circulated/Commemorative"]
        ]

        # 2. Генерация и сохранение монет по одной
        for _ in range(count):
            coin = CoinModel(
                country=fake.random_element(countries),
                nominal=fake.random_element(("1", "2", "5", "10", "20", "50", "100")),
                currency=fake.random_element(("рубль", "гривна", "тенге", "сом", "лари")),
                year=str(fake.random_int(min=1900, max=2023)),
                km_number=fake.bothify(text="KM# ??##"),
                material=fake.random_element(materials),
                state=fake.random_element(states),
                type_of_edition=fake.random_element(types_of_edition),
                edition=fake.random_int(min=1000, max=100000),
                weight=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                diameter=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                averse_image="default_pic/coin-01.jpg",
                reverse_image="default_pic/coin-02.jpg",
                in_collect=fake.boolean(),
                description=fake.text(max_nb_chars=200),
            )
            coin.save()
            selected_themes = fake.random_elements(themes, unique=True, length=3)
            coin.themes.set(selected_themes)

        # 3. Генерация и сохранение банкнот по одной
        for _ in range(count):
            banknote = BanknoteModel(
                country=fake.random_element(countries),
                nominal=fake.random_element(("1", "2", "5", "10", "20", "50", "100")),
                currency=fake.random_element(("рубль", "гривна", "тенге", "сом", "лари")),
                year=str(fake.random_int(min=1900, max=2023)),
                km_number=fake.bothify(text="KM# ??##"),
                material=fake.random_element(materials),
                state=fake.random_element(states),
                type_of_edition=fake.random_element(types_of_edition),
                signature=fake.name(),
                size=fake.bothify(text="##x## mm"),
                serial_number=fake.bothify(text="SN ######"),
                averse_image="default_pic/note-01.jpg",
                reverse_image="default_pic/note-02.jpg",
                in_collect=fake.boolean(),
                description=fake.text(max_nb_chars=200),
            )
            banknote.save()
            selected_themes = fake.random_elements(themes, unique=True, length=3)
            banknote.themes.set(selected_themes)

        self.stdout.write(
            self.style.SUCCESS(f"Успешно создано {count} записей для каждой модели.")
        )
