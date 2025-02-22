def generate_unique_slug(model_class, base_slug, slug_field="slug"):
    """Создает уникальный слаг объекта."""
    counter = 1
    temp_slug = base_slug
    while model_class.objects.filter(**{slug_field: temp_slug}).exists():
        temp_slug = f"{base_slug}-{counter}"
        counter += 1
    return temp_slug
