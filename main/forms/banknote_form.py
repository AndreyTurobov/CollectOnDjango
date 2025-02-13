from django import forms

from main.models.banknote_model import BanknoteModel


class BanknoteForm(forms.ModelForm):
    class Meta:
        """Метаданные формы BanknoteForm."""

        model = BanknoteModel
        exclude = [
            "created_at",
            "updated_at",
            "full_title",
            "slug",
        ]
        widgets = {
            "country": forms.Select(attrs={"class": "form-control"}),
            "material": forms.Select(attrs={"class": "form-control"}),
            "state": forms.Select(attrs={"class": "form-control"}),
            "type_of_edition": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 1}),
            "placeholder": "Введите описание банкноты",
        }
