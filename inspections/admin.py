from django.contrib import admin
from .models import (
    InspectionResult, Inspection, InspectionTrip
)

##########################################################################
""" Inspection Admin """
""" See Permit Models for Inspection Types, which was put there to 
prevent a circular reference. """
##########################################################################



@admin.register(InspectionResult)
class DivisionAdmin(admin.ModelAdmin):
    pass

@admin.register(Inspection)
class PermitStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(InspectionTrip)
class ReviewTypeAdmin(admin.ModelAdmin):
    pass

##########################################################################
""" End File """
##########################################################################