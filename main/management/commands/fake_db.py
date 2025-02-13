from django.core.management.base import BaseCommand

from faker import Faker

from main.models.banknote_model import BanknoteModel
from main.models.choice_models import Country, Material, State, TypeOfEdition
from main.models.coin_model import CoinModel


class Command(BaseCommand):
    help = "Заполняет базу данных фейковыми данными для моделей Coin и Banknote."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=10,
            help="Количество записей для каждой модели (по умолчанию 10).",
        )

    def handle(self, *args, **options):
        fake = Faker()
        count = options["count"]

        # Создаем или получаем объекты для ForeignKey полей
        countries = [
            Country.objects.get_or_create(title=title)[0]
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
            ]
        ]

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

        types_of_edition = [
            TypeOfEdition.objects.get_or_create(title=title)[0]
            for title in ["Commemorative", "Circulated", "Circulated/Commemorative"]
        ]

        for _ in range(count):
            coin = CoinModel(
                country=fake.random_element(elements=countries),
                nominal=fake.random_element(elements=("1", "2", "5", "10", "20", "50", "100")),
                currency=fake.random_element(elements=("рубль", "гривна", "тенге", "сом", "лари")),
                year=str(fake.random_int(min=1900, max=2023)),
                km_number=fake.bothify(text="KM# ??##"),
                material=fake.random_element(elements=materials),
                state=fake.random_element(elements=states),
                in_collect=fake.boolean(),
                description=fake.text(max_nb_chars=200),
                type_of_edition=fake.random_element(elements=types_of_edition),
                edition=fake.random_int(min=1000, max=100000),
                weight=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                diameter=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                averse_image="default_pic/coin-01.jpg",
                reverse_image="default_pic/coin-02.jpg",
            )
            coin.save()

        for _ in range(count):
            banknote = BanknoteModel(
                country=fake.random_element(elements=countries),
                nominal=fake.random_element(elements=("1", "2", "5", "10", "20", "50", "100")),
                currency=fake.random_element(elements=("рубль", "гривна", "тенге", "сом", "лари")),
                year=str(fake.random_int(min=1900, max=2023)),
                km_number=fake.bothify(text="KM# ??##"),
                material=fake.random_element(elements=materials),
                state=fake.random_element(elements=states),
                in_collect=fake.boolean(),
                description=fake.text(max_nb_chars=200),
                type_of_edition=fake.random_element(elements=types_of_edition),
                signature=fake.name(),
                size=fake.bothify(text="##x## mm"),
                serial_number=fake.bothify(text="SN ######"),
                averse_image="default_pic/note-01.jpg",
                reverse_image="default_pic/note-02.jpg",
            )
            banknote.save()

        self.stdout.write(
            self.style.SUCCESS(f"Успешно создано {count} записей для каждой модели.")
        )
