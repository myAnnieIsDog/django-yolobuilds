"""
This file was to test an idea of putting each app in a single file.
While working on the app it has it's conveniences, but when just working
on, for example, views, this approach greatly increases the number of
files that would have to be opened and edited. The standard approach
appears to balance locality of behavior with clustering similar functions
for a handful of models into a single app.

"""
##########################################################################
""" App Config """
##########################################################################

from django.apps import AppConfig
class TagConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tags'
    verbose_name = "Tag"
    verbose_name_plural = "Tags"


##########################################################################
""" Models """
##########################################################################

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
class Tag(models.Model):      
    tag = models.CharField(max_length=100, unique=True)
    policy = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.tag   

class TaggedRecord(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    policy = models.CharField(max_length=255, null=True, blank=True)

    lock = models.BooleanField(
        "Lock this record?", default=False)
    lock_related = models.BooleanField(
        "Lock related records?", default=False)
    alert = models.BooleanField(
        "Popup notification on this record?", default=True)
    alert_related = models.BooleanField(
        "Popup notification on related records?", default=False)

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self) -> str:
        return self.tag.tag
    
    class Meta:
        indexes = [models.Index(fields=["content_type", "object_id",],),]
        verbose_name = "Tagged Record"
        verbose_name_plural = "Tagged Records"


##########################################################################
""" Views """
##########################################################################

from django.views.generic import ListView
class TagList(ListView):
    model = Tag


##########################################################################
""" URL's """
##########################################################################

from django.urls import path
from django.views.generic import TemplateView

app_name = "tags"
urlpatterns = [
    path('list/<tag:str>', 
        TagList.as_view(template_name="reviews/cycle_prototype.html"), 
        name="review_detail"),

    path('detail/<tag:str>', 
        TemplateView.as_view(template_name="reviews/cycle_prototype.html"), 
        name="review_detail"),
]

##########################################################################
""" Admin """
##########################################################################

from django.contrib import admin

class TaggedRecordInline():
    model = TaggedRecord

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = TaggedRecordInline


##########################################################################
""" End File """
##########################################################################