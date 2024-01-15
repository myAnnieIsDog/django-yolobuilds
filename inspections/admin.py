from django.contrib import admin
from .models import (
    InspectionType, InspectionResult, Inspection, InspectionTrip, InspectionGroup
)

##########################################################################
""" Inspection Admin """
""" See Permit Models for Inspection Types, which was put there to 
prevent a circular reference. """
##########################################################################

@admin.register(InspectionGroup)
class InspectionGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(InspectionType)
class InspectionTypeAdmin(admin.ModelAdmin):
    list_display = ["inspection_type", "insp_group", "default_inspector", "duration_hours", "trip_factor"]
    list_editable = ["insp_group", "default_inspector", "duration_hours", "trip_factor"]
    list_filter = ["insp_group"]


@admin.register(InspectionResult)
class InspectionResultAdmin(admin.ModelAdmin):
    list_display = ["result", "requirements"]

@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    pass

@admin.register(InspectionTrip)
class InspectionTripAdmin(admin.ModelAdmin):
    pass

##########################################################################
""" End File """
##########################################################################