from django.test import RequestFactory

import pytest

from main.models.banknote_model import BanknoteModel
from main.models.choice_models import (
    Country,
    Material,
    State,
    TypeOfEdition,
)
from main.models.coin_model import CoinModel


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.fixture
def country(db):
    return Country.objects.create(title="Test Country", flag="test.jpg")


@pytest.fixture
def material(db):
    return Material.objects.create(title="Gold")


@pytest.fixture
def state(db):
    return State.objects.create(title="UNC")


@pytest.fixture
def edition(db):
    return TypeOfEdition.objects.create(title="Regular")


@pytest.fixture
def banknote(db, country, material, state, edition):
    return BanknoteModel.objects.create(
        country=country,
        material=material,
        state=state,
        type_of_edition=edition,
        nominal="10",
        year="2020",
        km_number="123",
        currency="USD",
        description="Test banknote",
        size="100*50",
    )


@pytest.fixture
def coin(db, country, material, state, edition):
    return CoinModel.objects.create(
        country=country,
        material=material,
        state=state,
        type_of_edition=edition,
        nominal="1",
        year="2021",
        km_number="456",
        currency="USD",
        description="Test coin",
        edition=1000,
        diameter=20,
        weight=5,
    )
