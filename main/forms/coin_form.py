from django import forms

from main.models.coin_model import CoinModel


class CoinForm(forms.ModelForm):
    class Meta:
        """Метаданные формы CoinForm."""

        model = CoinModel
        fields = "__all__"
