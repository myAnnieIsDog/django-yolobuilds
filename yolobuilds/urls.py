"""
URL configuration for yolobuilds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

admin.site.site_title = 'Yolo Builds'
admin.site.site_header = 'Yolo Builds'
admin.site.index_title = 'Site Administration'

urlpatterns = [
    
    # Permit modules
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    # path('bl/', include('permits_bl.urls')),  
    path('bp/', include('permits_bp.urls')), 
    # path('ce/', include('permits_ce.urls')),
    # path('pw/', include('permits_pw.urls')),  
    # path('zf/', include('permits_zf.urls')),  

    # Admin/Config
    path('admin/', admin.site.urls, name="admin"),
    path('fees/', include('fees.urls')),
    # path('licenses/', include('licenses.urls'), name="licenses"),  
    path('locations/', include('locations.urls'), name="locations"),    
    # path('payments/', include('payments.urls')),  
    path('profiles/', include('profiles.urls')),
    path('reviews/', include('reviews.urls')),
    path('users/', include('django.contrib.auth.urls'), name="users"),
]