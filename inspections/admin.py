from django.contrib import admin
from .models import (
    InspectionType, InspectionResult, Inspection, InspectionTrip
)

##########################################################################
""" Inspection Admin """
""" See Permit Models for Inspection Types, which was put there to 
prevent a circular reference. """
##########################################################################

@admin.register(InspectionType)
class InspectionTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(InspectionResult)
class InspectionResultAdmin(admin.ModelAdmin):
    pass

@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    pass

@admin.register(InspectionTrip)
class InspectionTripAdmin(admin.ModelAdmin):
    pass

##########################################################################
""" End File """
##########################################################################