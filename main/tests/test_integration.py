from django.test import Client, TestCase
from django.urls import reverse

import pytest


class TestBanknoteViews(TestCase):
    @pytest.mark.django_db
    def setUp(self):
        self.client = Client()
        self.url = reverse("banknote-list")

    def test_view_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "banknotes/list_banknotes.html")
