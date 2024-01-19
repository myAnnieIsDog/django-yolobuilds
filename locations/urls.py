from django.urls import path
from django.views.generic.base import TemplateView
from .views import ParcelSearch, ParcelDetail, AddressSearch, AddressDetail
app_name = "location"
urlpatterns = [
    path('apn/search/',
         ParcelSearch.as_view(template_name="location/apn_search.html"), 
         name="apn-search"
    ),
    path('apn/detail/', 
         ParcelDetail.as_view(template_name="location/apn_detail.html"), 
         name="apn-detail"
    ),
    path('address/search/', 
         AddressSearch.as_view(template_name="location/address_search.html"), 
         name="address-search"
    ),
    path('address/<address>/', 
         AddressDetail.as_view(template_name="location/address_detail.html"), 
         name="address-detail"
    ),
]