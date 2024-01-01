from django.urls import path
from django.views.generic.base import TemplateView

app_name = "permits"
urlpatterns = [

    path('reviews/list/', 
        TemplateView.as_view(template_name="review.html"), 
        name="review_list"),
]