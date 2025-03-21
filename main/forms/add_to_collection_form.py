from django import forms


class AddToCollectionForm(forms.Form):
    collection = forms.ChoiceField(
        label="Выберите коллекцию",
        widget=forms.Select(attrs={"class": "w-full p-2 border rounded"}),
    )

    def __init__(self, *args, collections=None, **kwargs):
        """Инициализация формы с выбором коллекции для добавления объекта."""
        super().__init__(*args, **kwargs)
        if collections:
            self.fields["collection"].choices = [
                (collection.slug, collection.title) for collection in collections
            ]
