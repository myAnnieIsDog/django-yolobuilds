from django.apps import AppConfig

class GeneralConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'general'
    verbose_name = "General"
    verbose_name_plural = "General"
