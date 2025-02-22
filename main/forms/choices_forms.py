from django import forms

from main.models.choice_models import (
    Country,
    Material,
    State,
    Theme,
    TypeOfEdition,
)


class CountryForm(forms.ModelForm):
    class Meta:
        """Метаданные формы CountryForm."""

        model = Country
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "rows": 1,
                    "class": "w-full px-4 py-2 rounded-lg border border-[#581c87]",
                    "placeholder": "Страна",
                }
            )
        }


class MaterialForm(forms.ModelForm):
    class Meta:
        """Метаданные формы MaterialForm."""

        model = Material
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "rows": 1,
                    "class": "w-full px-4 py-2 rounded-lg border border-[#581c87]",
                    "placeholder": "Материал",
                }
            )
        }


class StateForm(forms.ModelForm):
    class Meta:
        """Метаданные формы StateForm."""

        model = State
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "rows": 1,
                    "class": "w-full px-4 py-2 rounded-lg border border-[#581c87]",
                    "placeholder": "Состояние",
                }
            )
        }


class ThemeForm(forms.ModelForm):
    class Meta:
        """Метаданные формы ThemeForm."""

        model = Theme
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "rows": 1,
                    "class": "w-full px-4 py-2 rounded-lg border border-[#581c87]",
                    "placeholder": "Тема",
                }
            )
        }


class TypeOfEditionForm(forms.ModelForm):
    class Meta:
        """Метаданные формы TypeOfEditionForm."""

        model = TypeOfEdition
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "rows": 1,
                    "class": "w-full px-4 py-2 rounded-lg border border-[#581c87]",
                    "placeholder": "Тип издания",
                }
            )
        }
