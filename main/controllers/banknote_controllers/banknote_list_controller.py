from django.views.generic import ListView

from main.models.base import CollectorsItem
from main.services.banknote_service import BanknoteService


class BanknoteListController(ListView):
    template_name = 'banknotes/list.html'
    context_object_name = 'banknotes'
    paginate_by = 9

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = BanknoteService()

    def get_context_data(self, **kwargs):
        # Добавляем CHOICES в контекст шаблона
        context = super().get_context_data(**kwargs)
        context['COUNTRY_CHOICES'] = CollectorsItem.COUNTRY_CHOICES
        context['MATERIAL_CHOICES'] = CollectorsItem.MATERIAL_CHOICES
        context['STATE_CHOICES'] = CollectorsItem.STATE_CHOICES
        context['TYPE_OF_EDITION_CHOICES'] = CollectorsItem.TYPE_OF_EDITION_CHOICES
        return context

    def get_queryset(self):
        # Получаем параметры фильтрации из запроса
        filters = {
            'full_title__icontains': self.request.GET.get('name', ''),
            'country': self.request.GET.get('country', ''),
            'year': self.request.GET.get('year', ''),
            'km_number': self.request.GET.get('km_number', ''),
            'material': self.request.GET.get('material', ''),
            'state': self.request.GET.get('state', ''),
            'type_of_edition': self.request.GET.get('type_of_edition', ''),
        }
        # Используем сервис для поиска банкнот
        return self.service.get_by_filter(filters).order_by('id')
