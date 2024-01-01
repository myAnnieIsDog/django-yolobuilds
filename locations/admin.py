from django.contrib import admin
from .models import (
    DistrictType, District, Jurisdiction, Parcel, SiteAddress
)
##########################################################################
""" Location Admin """
##########################################################################

class DistrictInline(admin.StackedInline):
    model = District
    extra = 1

@admin.register(DistrictType)
class DistrictTypeAdmin(admin.ModelAdmin):
    inlines = [DistrictInline]

# @admin.register(District)
# class DistrictAdmin(admin.ModelAdmin):
#     list_display = ["name", "type", "description"]

@admin.register(Jurisdiction)
class JurisdictionAdmin(admin.ModelAdmin):
    pass

class AddressInline(admin.StackedInline):
    model = SiteAddress
    extra = 1

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    inlines = [AddressInline]

# @admin.register(SiteAddress)
# class SiteAddressAdmin(admin.ModelAdmin):
#     pass

##########################################################################
""" End File """
##########################################################################