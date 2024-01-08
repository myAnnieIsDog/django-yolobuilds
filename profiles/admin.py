##########################################################################
""" Profile Admin """
##########################################################################
from django.contrib import admin
from .models import (Profile, LicenseAgency, LicenseType, LicenseHolder, 
    Agency, YoloCountyPartners, Department, Division, 
    Staff)

@admin.register(Agency)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Agency Option"
    verbose_name_plural = "Agency Options"

@admin.register(Department)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Department Option"
    verbose_name_plural = "Department Options"

@admin.register(Division)
class ProfilesAdmin(admin.ModelAdmin):
    verbose_name = "Division Option"
    verbose_name_plural = "Division Options"


class LicenseTypeInline(admin.TabularInline):
    model = LicenseType
    extra = 3
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
    extra = 3
class YoloCountyPartnersInline(admin.TabularInline):
    model = YoloCountyPartners
    extra = 3
class StaffInline(admin.TabularInline):
    model = Staff
    extra = 3
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