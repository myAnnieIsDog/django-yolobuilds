from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
  

##########################################################################
""" Tags """
##########################################################################

class Tag(models.Model):      
    tag = models.CharField(max_length=100, unique=True)
    policy = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.tag   

class TaggedRecord(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    details = models.CharField(max_length=255, null=True, blank=True)

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
""" Related Records """
##########################################################################


class RelatedRecord(models.Model):
    parent_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="parenteroo")
    parent_id = models.PositiveIntegerField()
    parent_object = GenericForeignKey("parent_type", "parent_id")

    child_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="childeroo")
    child_id = models.PositiveIntegerField()
    child_object = GenericForeignKey("child_type", "child_id")

    def __str__(self) -> str:
        return f"{self.parent_object} - {self.child_object}"

    class Meta:
        indexes = [models.Index(fields=[
                "parent_type", "parent_id",
                "child_type", "child_id",],),]
        verbose_name = "Related Record"
        verbose_name_plural = "Related Records"
   
##########################################################################
""" All Models """
##########################################################################
all_models = (
    Tag,
    TaggedRecord,
    RelatedRecord,
)
##########################################################################
""" End File """
##########################################################################