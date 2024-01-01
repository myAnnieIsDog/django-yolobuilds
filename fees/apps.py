from django.apps import AppConfig


class FeesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fees'
    verbose_name = "Fee Schedule"
    verbose_name_plural = "Fee Schedule"
