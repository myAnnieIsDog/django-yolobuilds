from django.contrib import admin
from .models import (
    District, Jurisdiction, Parcel, SiteAddress
)
##########################################################################
""" Location Admin """
##########################################################################


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ["dist_type", "district", "description"]

@admin.register(Jurisdiction)
class JurisdictionAdmin(admin.ModelAdmin):
    pass

class AddressInline(admin.StackedInline):
    model = SiteAddress
    extra = 1

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    inlines = [AddressInline]

@admin.register(SiteAddress)
class SiteAddressAdmin(admin.ModelAdmin):
    pass

##########################################################################
""" End File """
##########################################################################