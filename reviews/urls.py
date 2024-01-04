from django.urls import path
from django.views.generic.base import TemplateView

app_name = "permits"
urlpatterns = [

    path('', 
        TemplateView.as_view(template_name="reviews/cycles.html"), 
        name="review_list"),
]