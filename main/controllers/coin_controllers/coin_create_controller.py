from django.views.generic import CreateView

from main.forms.coin_form import CoinForm


class CoinCreateController(CreateView):
    form_class = CoinForm
    template_name = "coins/create_coin.html"
    success_url = "/coins/"

    def get_context_data(self, **kwargs):
        """Добавляет контекст для использования в шаблоне."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавление монеты"
        context["breadcrumbs"] = [
            {"title": "Главная", "url": "/"},
            {"title": "Монеты", "url": "/coins/"},
            {"title": "Добавить монету", "url": ""},
        ]
        return context

    def form_valid(self, form):
        """Сохраняет монету в базе данных."""
        coin = form.save(commit=False)
        coin.save()
        return super().form_valid(form)
