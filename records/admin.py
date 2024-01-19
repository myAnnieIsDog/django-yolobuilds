##########################################################################
""" Register Record Base Models with the Admin Interface """
##########################################################################
from django.contrib import admin
from .models import Division, Tag, Restriction, Status, Type, Record


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag", "policy"]
    list_display_links = ["tag", "policy"]
    ordering = ["tag"]

@admin.register(Restriction)
class RestrictionAdmin(admin.ModelAdmin):
    pass

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["status", "policy", "build", "occupy"]
    list_editable = ["policy", "build", "occupy"]
    ordering = ["status"]

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["division", "prefix", "type", "suffix", "policy"]
    list_display_links = ["division", "prefix", "policy"] 
    list_editable = ["type", "suffix"]

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
    
##########################################################################
""" End File """
##########################################################################