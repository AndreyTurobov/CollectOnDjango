from django.core.management.base import BaseCommand

from faker import Faker

from main.models.coin_model import CoinModel
from main.models.banknote_model import BanknoteModel


class Command(BaseCommand):
    help = 'Заполняет базу данных фейковыми данными для моделей Coin и Banknote.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Количество записей для каждой модели (по умолчанию 10).',
        )

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']

        # Заполнение модели Coin
        for _ in range(count):
            CoinModel.objects.create(
                country=fake.random_element(elements=(
                    'Россия', 'Украина', 'Беларусь', 'Казахстан', 'Таджикистан',
                    'Киргизия', 'Азербайджан', 'Армения', 'Грузия', 'Молдова',
                    'Туркменистан', 'Узбекистан', 'Латвия', 'Литва', 'Эстония', 'Польша'
                )),
                nominal=fake.random_element(elements=('1', '2', '5', '10', '20', '50', '100')),
                currency=fake.random_element(elements=('рубль', 'гривна', 'тенге', 'сом', 'лари')),
                year=fake.random_int(min=1900, max=2023),
                km_number=fake.bothify(text='KM# ??##'),
                material=fake.random_element(elements=(
                    'Серебро', 'Золото', 'Бронза', 'Никель', 'Медь', 'Латунь', 'Сталь',
                    'Алюминий', 'Нейзильбер', 'Мельхиор', 'Цинковый сплав', 'Алюминиевая бронза',
                    'Биметалл', 'Пластик', 'Бумага'
                )),
                state=fake.random_element(elements=(
                    'Proof_like', 'BUNC', 'UNC', 'AUNC', 'XF', 'VF'
                )),
                in_collect=fake.boolean(),
                description=fake.text(max_nb_chars=200),
                type_of_edition=fake.random_element(elements=(
                    'Commemorative', 'Circulated', 'Circ/Comm'
                )),
                edition=fake.random_int(min=1000, max=100000),
                weight=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                diameter=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
            )

        # Заполнение модели Banknote
        for _ in range(count):
            BanknoteModel.objects.create(
                country=fake.random_element(elements=(
                    'Россия', 'Украина', 'Беларусь', 'Казахстан', 'Таджикистан',
                    'Киргизия', 'Азербайджан', 'Армения', 'Грузия', 'Молдова',
                    'Туркменистан', 'Узбекистан', 'Латвия', 'Литва', 'Эстония', 'Польша'
                )),
                nominal=fake.random_element(elements=('1', '2', '5', '10', '20', '50', '100')),
                currency=fake.random_element(elements=('рубль', 'гривна', 'тенге', 'сом', 'лари')),
                year=fake.random_int(min=1900, max=2023),
                km_number=fake.bothify(text='KM# ??##'),
                material=fake.random_element(elements=(
                    'Серебро', 'Золото', 'Бронза', 'Никель', 'Медь', 'Латунь', 'Сталь',
                    'Алюминий', 'Нейзильбер', 'Мельхиор', 'Цинковый сплав', 'Алюминиевая бронза',
                    'Биметалл', 'Пластик', 'Бумага'
                )),
                state=fake.random_element(elements=(
                    'Proof_like', 'BUNC', 'UNC', 'AUNC', 'XF', 'VF'
                )),
                in_collect=fake.boolean(),
                description=fake.text(max_nb_chars=200),
                type_of_edition=fake.random_element(elements=(
                    'Commemorative', 'Circulated', 'Circ/Comm'
                )),
                signature=fake.name(),
                size=fake.bothify(text='##x## mm'),
                serial_number=fake.bothify(text='SN ######'),
            )

        self.stdout.write(self.style.SUCCESS(f'Успешно создано {count} записей для каждой модели.'))
