##########################################################################
""" Review Admin """
##########################################################################
from django.contrib import admin
from .models import ReviewStatus, ReviewCycle, ReviewType, Review

@admin.register(ReviewType)
class InspectionTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewStatus)
class DivisionAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class PermitStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewCycle)
class ReviewTypeAdmin(admin.ModelAdmin):
    pass

##########################################################################
""" End File """
##########################################################################