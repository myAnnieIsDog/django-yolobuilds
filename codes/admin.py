from django.contrib import admin

from .models import Authority, Code, Chapter, Section, Requirement

class CodeInline(admin.TabularInline):
    model = Code
    show_change_link = True
    extra = 0

class ChapterInline(admin.TabularInline):
    model = Chapter
    ordering = ["number"]
    show_change_link = True
    extra = 0

class SectionInline(admin.TabularInline):
    model = Section
    show_change_link = True
    extra = 0

class RequirementInline(admin.StackedInline):
    model = Requirement
    show_change_link = True
    extra = 0


@admin.register(Authority)
class AuthorityAdmin(admin.ModelAdmin):
    list_display = ["name", "full_name"]
    list_display_links = ["name", "full_name"]
    ordering = ["name", "full_name"]
    inlines = [CodeInline]
    name = "Authority"


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ["title", "full_title"]
    list_display_links = ["title", "full_title"]
    ordering = ["title", "full_title"]
    inlines = [ChapterInline]
    name = "Code"

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ["number", "title", "full_title"]
    list_display_links = ["number", "title", "full_title"]
    ordering = ["number", "title", "full_title"]
    inlines = [SectionInline]
    name = "Chapter"

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ["number", "title", "full_title"]
    list_display_links = ["number", "title", "full_title"]
    ordering = ["number", "title", "full_title"]
    inlines = [RequirementInline]
    name = "Section"

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "answer"]
    list_editable = ["text", "answer"]
    ordering = ["title", "text", "answer"]
    name = "Requirement"


""" Template """
# class CodeInline(admin.TabularInline):
#     model = Code
#     extra = 0
#
# @admin.register(Code)
# class CodeAdmin(admin.ModelAdmin):
#     list_display = ["", ""]
#     list_display_links = ["", ""]
#     list_filter = ["", ""]
#     list_editable = ["", ""]
#     ordering = ["", ""]
#     actions_on_bottom = True
#     inlines = ["", ""]
#     name = ""

"""  
https://stackoverflow.com/questions/70145579/how-could-i-display-parent-object-attribute-in-django-admin
"""
# admin.site.register(UserTrainer, CustomUserAdmin)
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('article', 'slug','trainer')
#     list_display_links = ('article',)
#     fields = ('article', 'slug', 'keywords', 'text',)
#     readonly_fields = ('trainer',)

#     def save_model(self, request, obj, form, change):
#         obj.trainer = request.user
#         super().save_model(request, obj, form, change)
