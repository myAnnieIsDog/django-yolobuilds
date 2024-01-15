##########################################################################
""" Buiding Permit Admin """
##########################################################################
from django.contrib import admin
from .models import (
    BP, Building, Demolition, Electrical, Fire, Flood, Grading, 
    Mechanical, Plumbing, Pool, ApplicantRole, OwnerRole, FloodZones
)


# @admin.register(ApplicantRole)
# class ApplicantRoleAdmin(admin.ModelAdmin):
#     pass


# @admin.register(OwnerRole)
# class OwnerRoleAdmin(admin.ModelAdmin):
#     pass

# @admin.register(BP)
# class DivisionAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Building)
# class ReviewTypeAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Demolition)
# class InspectionTypeAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Electrical)
# class PermitStatusAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Fire)
# class PermitTypeAdmin(admin.ModelAdmin):
#     pass

# @admin.register(FloodZones)
# class FloodZonesAdmin(admin.ModelAdmin):
#     list_display = ["zone_code", "zone_description"]
#     list_display_links = ["zone_code", "zone_description"]
    
# @admin.register(Flood)
# class FloodAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Grading)
# class PermitAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Mechanical)
# class PermitAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Plumbing)
# class PermitAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Pool)
# class PermitAdmin(admin.ModelAdmin):
#     pass

##########################################################################
""" End """
##########################################################################