from typing import Any

from django import forms

from main.models.coin_model import CoinModel


class CoinForm(forms.ModelForm):
    class Meta:
        """Метаданные формы CoinForm."""

        model: type[CoinModel] = CoinModel
        exclude: list[str] = [
            "created_at",
            "updated_at",
            "full_title",
            "slug",
        ]
        widgets: dict[str, Any] = {
            "country": forms.Select(attrs={"class": "form-control"}),
            "material": forms.Select(attrs={"class": "form-control"}),
            "state": forms.Select(attrs={"class": "form-control"}),
            "themes": forms.SelectMultiple(attrs={"class": "form-control"}),
            "type_of_edition": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 1}),
            "placeholder": "Введите описание монеты",
        }
