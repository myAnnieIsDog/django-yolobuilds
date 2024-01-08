from django.shortcuts import render
from django.views.generic import ListView
from locations.models import SiteAddress, Parcel, District


class AddressSearch(ListView):
    model = SiteAddress


