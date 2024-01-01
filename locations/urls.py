from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('locations/', TemplateView.as_view(
        template_name="locations/locations.html")),
]