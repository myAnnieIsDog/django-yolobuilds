##########################################################################
""" Permit Base Models """
##########################################################################
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from locations.models import Parcel, SiteAddress
from profiles.models import Division, Profile

##########################################################################
""" Sequence Counts """
##########################################################################
class Sequence(models.Model):
    series_title = models.CharField(max_length = 55)
    series_prefix = models.CharField(max_length=2)
    year = models.DateTimeField(default=timezone.now().strftime("%Y"))
    sequence = models.CharField(max_length=4, default="0000")

    def __str__(self) -> str:
        return self.series  
    # BL, BP, CE, PW, ZF, Receipt, etc.

    def next(series): # <- series title
        n = Sequence.objects.get(series_title=series)
        n.year = timezone.now().strftime("%Y")
        n.sequence = str(int(n.sequence) + 1)
        while len(n.sequence) < 4:
            n.sequence = f"0{n.sequence}"
        return f"{n.series}{n.year}-{n.sequence}"


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
""" Permit Options """
##########################################################################
class Division(models.Model): 
    prefix = models.CharField(max_length=2, unique=True) 
    title = models.CharField(max_length=30, unique=True) 

    def __str__(self) -> str:
        return self.prefix

class PermitStatus(models.Model): 
    status = models.CharField(max_length=30, unique=True)
    policy = models.CharField(max_length=255)
    build = models.BooleanField(default=False)
    occupy = models.BooleanField(default=False)

    class Meta():
        verbose_name = "Permit Status"
        verbose_name_plural = "Permit Statuses"

class PermitType(models.Model): 
    type = models.CharField(max_length=255, unique=True)
    policy = models.CharField(max_length=255)
    suffix = models.CharField(max_length=7, default="Ex-R", unique=True)

    class Meta():
        verbose_name = "Permit Type"
        verbose_name_plural = "Permit Types"

class PermitSubtype(models.Model): 
    type = models.ForeignKey(PermitType, on_delete=models.PROTECT)
    subtype = models.CharField(max_length=255, unique=True)
    policy = models.CharField(max_length=255)

    class Meta():
        verbose_name = "Permit Subtype"
        verbose_name_plural = "Permit Subtypes"

    
##########################################################################
""" Permit Model """
##########################################################################
class Permit(models.Model):
    number = models.CharField(max_length=55, blank=True)
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    type = models.ForeignKey(PermitType, on_delete=models.PROTECT)
    subtype = models.ForeignKey(PermitSubtype, on_delete=models.PROTECT)
    description = models.TextField()

    status = models.ForeignKey(PermitStatus, on_delete=models.PROTECT)
    
    apn = models.ForeignKey(
        Parcel, on_delete=models.PROTECT, null=True, blank=True)
    address = models.ForeignKey(
        SiteAddress, on_delete=models.PROTECT, null=True, blank=True)
    owner = models.ForeignKey(
        Profile, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="ownries")
    applicant = models.ForeignKey(
        Profile, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="apper")

    def __str__(self) -> str:
        return f"{self.number}"

    class Meta():
        ordering = ["number"]
        verbose_name = "Permit"
        verbose_name_plural = "Permits"


##########################################################################
""" All Models """
##########################################################################
"""This list only includes models that are in their stable form."""
all_models = (
    Tag,
    TaggedRecord,
    RelatedRecord,
    Division,
    PermitStatus,
    PermitType,
    PermitSubtype,
    Permit,
)
##########################################################################
""" End File """
##########################################################################