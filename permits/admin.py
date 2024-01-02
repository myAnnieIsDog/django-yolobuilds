##########################################################################
""" Register Permit Base Models with the Admin Interface """
##########################################################################
from django.contrib import admin
from .models import Division, PermitStatus, PermitType, PermitSubtype, Permit

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    pass

@admin.register(PermitStatus)
class PermitStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(PermitType)
class PermitTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(PermitSubtype)
class PermitSubtypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Permit)
class PermitAdmin(admin.ModelAdmin):
    pass

##########################################################################
""" End File """
##########################################################################