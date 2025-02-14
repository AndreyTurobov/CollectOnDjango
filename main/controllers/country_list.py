from django.views.generic import ListView

from main.models.choice_models import Country


class CountryListView(ListView):
    model = Country
    template_name = "countries/countries_list.html"
    context_object_name = "countries"
