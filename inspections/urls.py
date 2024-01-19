from django.urls import path
from django.views.generic.base import TemplateView
app_name = "inspections"
urlpatterns = [
    path('request/', 
         TemplateView.as_view(template_name="insp_req.html"), 
         name="insp_req"),

    path('list/', 
         TemplateView.as_view(template_name="inspect.html"), 
         name="inspection_list"),

    path('route/', 
         TemplateView.as_view(template_name="insp_req.html"), 
         name="inspection_route"),
]