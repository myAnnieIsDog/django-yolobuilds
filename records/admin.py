##########################################################################
""" Register Record Base Models with the Admin Interface """
##########################################################################
from django.contrib import admin
from .models import Number, Tag, Restriction, Form, Question, Status, Type, Record, ContactType, Contact


# class TagInline(admin.TabularInline):
#     model = Tag
#     extra = 0
# class RestrictionInline(admin.TabularInline):
#     model = Restriction
#     extra = 0

# @admin.register(Number)
# class NumberAdmin(admin.ModelAdmin):
#     pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag", "policy"]
    list_display_links = ["tag", "policy"]
    ordering = ["tag"]

# @admin.register(Restriction)
# class RestrictionAdmin(admin.ModelAdmin):
#     pass

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ["form", "description"]
    list_editable = ["description"]
    ordering = ["form"]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
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
    list_display = [
        "division", 
        "status",
        "number",
        "description",
    ]
    list_display_links = [
        "division", 
        "status",
        "number",
    ]
    list_filter = ["division", "status"]
    list_editable = ["description"]
    ordering = [
        "division", 
        "status",
        "number",
        "description",
    ]
    actions_on_bottom = True
    # inlines = [TagInline, RestrictionInline]
    name = "Records"

@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ["role", "description"]
    list_editable = ["description"]
    ordering = ["role"]

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     pass

##########################################################################
""" End File """
##########################################################################