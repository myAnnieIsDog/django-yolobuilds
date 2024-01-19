##########################################################################
""" Profile Admin """
##########################################################################
from django.contrib import admin
from .models import (Profile, LicenseAgency, LicenseType, LicenseHolder, 
    Agency, YoloCountyPartners, Department, Division, 
    Staff)

@admin.register(Agency)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ["agency", "full_agency"]
    list_display_links = ["agency", "full_agency"]

@admin.register(Department)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ["dept_code", "department"]
    list_display_links = ["dept_code", "department"]

# @admin.register(Division)
# class ProfilesAdmin(admin.ModelAdmin):
#     list_display = ["prefix", "division", "full_division"]
#     list_display_links = ["prefix", "division", "full_division"]


class LicenseTypeInline(admin.TabularInline):
    model = LicenseType
    extra = 0
@admin.register(LicenseAgency)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Licensing Agency"
    verbose_name_plural = "Licensing Agencies"
    # inlines = [LicenseTypeInline]


@admin.register(LicenseType)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "License Type"
    verbose_name_plural = "License Types"



class LicenseHolderInline(admin.TabularInline):
    model = LicenseHolder
    extra = 0
class YoloCountyPartnersInline(admin.TabularInline):
    model = YoloCountyPartners
    extra = 0
class StaffInline(admin.TabularInline):
    model = Staff
    extra = 0
@admin.register(Profile)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Profile (all contacts)"
    verbose_name_plural = "Profiles (all contacts)"
    inlines = [
        LicenseHolderInline, 
        YoloCountyPartnersInline, 
        StaffInline
    ]

@admin.register(LicenseHolder)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Profile (license holders)"
    verbose_name_plural = "Profiles (license holders)"

@admin.register(YoloCountyPartners)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Profile (partners)"
    verbose_name_plural = "Profiles (partners)"

@admin.register(Staff)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Profile (staff)"
    verbose_name_plural = "Profiles (staff)"


##########################################################################
""" End """
##########################################################################