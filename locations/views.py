from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from locations.models import SiteAddress, Parcel, District
# from permits_bp.models import BP


class ParcelSearch(ListView):
    model = Parcel

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class ParcelDetail(DetailView):
    model = Parcel

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["districts"] = [District.objects.filter(parcel=self)]
        context["addresses"] = [SiteAddress.objects.filter(parcel=self)]
        # context["cases"] = [CE.objects.filter(parcel=self)]
        # context["licenses"] = [BL.objects.filter(parcel=self)]
        # context["planning"] = [ZF.objects.filter(parcel=self)]
        # context["public_works"] = [PW.objects.filter(parcel=self)]
        # context["building"] = [BP.objects.filter(parcel=self)]
        return context


class AddressSearch(ListView):
    model = SiteAddress
class AddressDetail(DetailView):
    model = SiteAddress

