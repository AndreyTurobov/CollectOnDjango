def generate_unique_slug(model, base_slug, instance=None):
    """Генерирует уникальный слаг, учитывая существующие записи.

    Если передается instance - исключаем его из проверки.
    """
    slug = base_slug
    counter = 1
    while True:
        qs = model.objects.filter(slug=slug)
        if instance:
            qs = qs.exclude(pk=instance.pk)
        if not qs.exists():
            return slug
        slug = f"{base_slug}-{counter}"
        counter += 1
