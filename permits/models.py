##########################################################################
""" Permit Base Models """
##########################################################################
from django.db import models
from django.utils import timezone
from general.models import Sequence

# from reviews.models import FeeType
from locations.models import Parcel, SiteAddress
from profiles.models import Profile


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


class WorkflowType(models.Model):
    # Expedited
    # Standard
    # Discretionary
    workflow = models.CharField(max_length=25, unique=True)
    description = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.workflow

    class Meta():
        ordering = ["workflow"]
        verbose_name = "Workflow Type"
        verbose_name_plural = "Workflow Types"

    
##########################################################################
""" Permit Model """
##########################################################################

class Permit(models.Model):
    number = models.ForeignKey(Sequence, on_delete=models.PROTECT)
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    type = models.ForeignKey(PermitType, on_delete=models.PROTECT)
    subtype = models.ForeignKey(PermitSubtype, on_delete=models.PROTECT)
    description = models.TextField()

    workflow_type = models.ForeignKey(WorkflowType, on_delete=models.PROTECT)

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
    Division,
    PermitStatus,
    PermitType,
    PermitSubtype,
    WorkflowType,
    Permit,
)
##########################################################################
""" End File """
##########################################################################