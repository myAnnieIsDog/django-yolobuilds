from django.contrib import admin
from .models import (
    District, Jurisdiction, Parcel, SiteAddress, CityStZip
)
##########################################################################
""" Location Admin """
##########################################################################
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ["dist_type", "district", "description"]
    list_display_links = ["dist_type", "district", "description"]
    list_filter = ["dist_type"]

@admin.register(Jurisdiction)
class JurisdictionAdmin(admin.ModelAdmin):
    pass

class AddressInline(admin.StackedInline):
    model = SiteAddress
    extra = 0
@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ["book", "page", "parcel"]
    list_display_links = ["book", "page", "parcel"]
    list_filter = ["book", "page"]
    inlines = [AddressInline]

@admin.register(CityStZip)
class CityStZipAdmin(admin.ModelAdmin):
    list_display = ["city", "state", "zip"]
    list_display_links = ["state"]
    list_editable = ["city", "zip"]

@admin.register(SiteAddress)
class SiteAddressAdmin(admin.ModelAdmin):
    list_display = ["number", "street", "city_st_zip", "parcel"]
    list_display_links = ["number", "street", "city_st_zip", "parcel"]
    list_filter = ["city_st_zip"]
##########################################################################
""" End File """
########################################################################## 