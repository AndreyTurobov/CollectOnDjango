from django import forms

from main.models.coin_model import CoinModel


class CoinForm(forms.ModelForm):
    class Meta:
        """Метаданные формы CoinForm."""

        model = CoinModel
        exclude = [
            "created_at",
            "updated_at",
            "full_title",
            "slug",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 1}),
            "placeholder": "Введите описание монеты",
        }
