from django.urls import path
from django.views.generic import TemplateView
from .models import Review
from .views import ReviewList, ReviewDetail


app_name = "permits"
urlpatterns = [

    path('', 
        TemplateView.as_view(template_name="reviews/cycle_prototype.html"), 
        name="review_detail"),
    
    path('list/', 
        ReviewList.as_view(template_name="reviews/list.html"), 
        name="review_list"),

    path('<int:pk>', 
        ReviewDetail.as_view(template_name="reviews/cycles.html"), 
        name="review_list"),
]