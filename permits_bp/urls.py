from django.urls import path
from django.views.generic.base import TemplateView

app_name = "bp"
urlpatterns = [

    path('', 
        TemplateView.as_view(template_name="permits_bp/home.html"), 
        name="home"),

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
        TemplateView.as_view(template_name="permits_bp/structural.html"), 
        name="structural"),


    path('application/', 
        TemplateView.as_view(template_name="permits_bp/apply.html"), 
        name="application"),




    path('app/accessory/', 
        TemplateView.as_view(template_name="permits_bp/accessory.html"),
        name="accessory"),

    path('app/commercial/', 
        TemplateView.as_view(template_name="permits_bp/commercial.html"),
        name="commercial"),

    path('app/demolition/', 
        TemplateView.as_view(template_name="permits_bp/demolition.html"),
        name="demolition"),
    
    path('app/dwelling/', 
        TemplateView.as_view(template_name="permits_bp/dwelling.html"),
        name="dwelling"),

    path('app/electrical/', 
        TemplateView.as_view(template_name="permits_bp/electrical.html"),
        name="electrical"),

    path('app/existing/',
        TemplateView.as_view(template_name="permits_bp/existing.html"),
        name="existing"),

    path('app/fire/', 
        TemplateView.as_view(template_name="permits_bp/fire.html"),
        name="fire"),

    path('app/flood/', 
        TemplateView.as_view(template_name="permits_bp/flood.html"),
        name="flood"),

    path('app/grading/',
        TemplateView.as_view(template_name="permits_bp/grading.html"), 
        name="grading"),

    path('app/mechanical/', 
        TemplateView.as_view(template_name="permits_bp/mechanical.html"), 
        name="mechanical"),

    path('app/plumbing/', 
        TemplateView.as_view(template_name="permits_bp/plumbing.html"), 
        name="plumbing"),

    path('app/pool/', 
        TemplateView.as_view(template_name="permits_bp/pool.html"), 
        name="pool"),
]