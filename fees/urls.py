from django.urls import path
from django.views.generic.base import TemplateView
from .views import FiscalDetailView


app_name = "fees"
urlpatterns = [
    path('fees/', FiscalDetailView.as_view(), name="fees"),
]