from django.urls import path
from django.views.generic.base import TemplateView

app_name = "bp"
urlpatterns = [

    path('', 
        TemplateView.as_view(template_name="permits_bp/home.html"), 
        name="home"),

    path('application/', 
        TemplateView.as_view(template_name="permits_bp/apply.html"), 
        name="application"),

    path('requests/', 
        TemplateView.as_view(template_name="permits_bp/requests.html"), 
        name="requests"),

    path('<int:year>/', 
        TemplateView.as_view(template_name="permits_bp/list.html"), 
        name="list"),

    path('<int:year>/<int:sequence>/', 
        TemplateView.as_view(template_name="permits_bp/detail.html"), 
        name="details"),

    path('structural/', 
        TemplateView.as_view(template_name="structural.html"), 
        name="structural"),
]