from django import forms

from main.models.banknote_model import BanknoteModel


class BanknoteForm(forms.ModelForm):
    class Meta:
        """Метаданные формы BanknoteForm."""

        model = BanknoteModel
        fields = "__all__"
