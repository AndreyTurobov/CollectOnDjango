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
