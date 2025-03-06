from django.views.generic import CreateView

from main.forms.banknote_form import BanknoteForm


class BanknoteCreateController(CreateView):
    form_class = BanknoteForm
    template_name = "banknotes/create_banknote.html"
    success_url = "/banknotes/"

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавление банкноты"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Банкноты", "url": "/banknotes/"},
            {"title": "Добавить банкноту", "url": ""},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет банкноту в базе данных."""
        banknote = form.save(commit=False)
        banknote.save()
        return super().form_valid(form)
