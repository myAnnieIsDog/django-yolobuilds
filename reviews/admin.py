##########################################################################
""" Review Admin """
##########################################################################
from django.contrib.admin import StackedInline 
from django.contrib import admin
from .models import ReviewStatus, ReviewCycle, ReviewType, Review, CycleResult

@admin.register(ReviewType)
class InspectionTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewStatus)
class DivisionAdmin(admin.ModelAdmin):
    pass

class ReviewCycleInline(StackedInline):
    model = ReviewCycle
    extra = 0
@admin.register(Review)
class PermitStatusAdmin(admin.ModelAdmin):
    inlines = [ReviewCycleInline]

@admin.register(ReviewCycle)
class ReviewTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(CycleResult)
class CycleResultAdmin(admin.ModelAdmin):
    pass

##########################################################################
""" End File """
##########################################################################