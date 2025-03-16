from typing import Any

from django import forms

from main.models.collection_model import CollectionModel


class CollectionForm(forms.ModelForm):
    class Meta:
        """Метаданные формы CollectionForm."""

        model: type[CollectionModel] = CollectionModel
        fields = ["title", "description"]
        widgets: dict[str, Any] = {
            "title": forms.TextInput(
                attrs={
                    "rows": 1,
                    "class": "w-full px-4 py-2 rounded-lg border border-[#581c87]",
                    "placeholder": "Название",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 1,
                    "class": "w-full px-4 py-2 rounded-lg border border-[#581c87]",
                    "placeholder": "Описание",
                }
            ),
        }
