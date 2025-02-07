from django import forms

from main.models.banknote_model import BanknoteModel


class BanknoteForm(forms.ModelForm):
    class Meta:
        """Метаданные формы BanknoteForm."""

        model = BanknoteModel
        fields = [
            "country",
            "nominal",
            "currency",
            "year",
            "km_number",
            "material",
            "state",
            "in_collect",
            "description",
            "type_of_edition",
            "signature",
            "size",
            "serial_number",
            "averse_image",
            "reverse_image",
        ]
