from django.apps import AppConfig


class FeesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fees'
    verbose_name = "Fees and Payment"
    verbose_name_plural = "Fees and Payments"
