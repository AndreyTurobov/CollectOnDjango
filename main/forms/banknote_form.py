from typing import Any

from django import forms

from main.models.banknote_model import BanknoteModel


class BanknoteForm(forms.ModelForm):
    class Meta:
        """Метаданные формы BanknoteForm."""

        model: type[BanknoteModel] = BanknoteModel
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
            "type_of_edition": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 1}),
            "placeholder": "Введите описание банкноты",
        }
