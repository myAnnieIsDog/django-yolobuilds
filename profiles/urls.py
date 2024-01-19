from django.urls import path
from .views import (ProfileCreateView, 
                    ProfileDetailView, 
                    ProfileUpdateView)
app_name = "profile"
urlpatterns = [
    path('create/', 
         ProfileCreateView.as_view(), 
         name="create"),

    path('detail/', 
         ProfileDetailView.as_view(), 
         name="detail"),

    path('update/', 
         ProfileUpdateView.as_view(), 
         name="update"),
]