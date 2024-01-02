from django.shortcuts import render
from django.views.generic import ListView
from locations.models import SiteAddress, Parcel, DistrictType, District


class AddressSearch(ListView):
    model = SiteAddress


