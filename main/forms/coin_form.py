from django import forms

from main.models.coin_model import CoinModel


class CoinForm(forms.ModelForm):
    class Meta:
        """Метаданные формы CoinForm."""

        model = CoinModel
        fields = [
            "country",
            "nominal",
            "currency",
            "year",
            "km_number",
            "edition",
            "material",
            "state",
            "in_collect",
            "description",
            "type_of_edition",
            "weight",
            "diameter",
            "averse_image",
            "reverse_image",
        ]
