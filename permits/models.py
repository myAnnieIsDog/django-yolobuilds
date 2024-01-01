##########################################################################
""" Permit Base Models """
##########################################################################
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from fees.models import FeeType
from locations.models import Parcel, SiteAddress
from profiles.models import Profile


class Division(models.Model): 
    prefix = models.CharField(max_length=2, unique=True) 
    title = models.CharField(max_length=30, unique=True) 

    def __str__(self) -> str:
        return self.prefix


class ReviewType(models.Model): 
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    review_type = models.CharField(max_length=30)
    days_cycle1 = models.PositiveSmallIntegerField(default=15)
    days_cycle2 = models.PositiveSmallIntegerField(default=5)
    default_reviewer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="revr")
    review_fees = models.ManyToManyField(FeeType)

    prerequisite = models.ManyToManyField("self")
    review_checklist = models.TextField(blank=True)
    add_next = models.ManyToManyField("self")

    def __str__(self) -> str:
        return self.type

    class Meta():
        verbose_name = "Review Type"
        verbose_name_plural = "Review Types"


class InspectionType(models.Model): 
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    inspection_type = models.CharField(max_length=30)
    default_inspector = models.ForeignKey(User, on_delete=models.PROTECT)
    duration_hours = models.DecimalField(
        max_digits=3, decimal_places=1, default=0.3)
    trip_factor = models.DecimalField(
        max_digits=7, decimal_places=2, default=1.20)
    inspection_fees = models.ManyToManyField(FeeType, blank=True)

    prerequisite = models.ManyToManyField("self", blank=True)
    inspection_checklist = models.TextField(blank=True)
    add_next = models.ManyToManyField("self", blank=True)
    
    
    def __str__(self) -> str:
        return self.type

    class Meta():
        verbose_name = "Inspection Type"
        verbose_name_plural = "Inspection Types"

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
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    type = models.ForeignKey(PermitType, on_delete=models.PROTECT)
    subtype = models.ForeignKey(PermitSubtype, on_delete=models.PROTECT)
    description = models.TextField()

    workflow_type = models.ForeignKey(WorkflowType, on_delete=models.PROTECT)
    year = models.SmallIntegerField(default=timezone.now().strftime("%Y"))
    sequence = models.CharField(max_length=4, default="0000")
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

    # inspections = models.ManyToManyField(InspectionType)
    # reviews = models.ManyToManyField(ReviewType)
    # fees = models.ManyToManyField(FeeType) 

    # files_confidential = models.FileField(upload_to='', storage=None, max_length=100)
    # files_public = models.FileField(upload_to='', storage=None, max_length=100)
    
    # application_package = models.FileField(upload_to='', storage=None, max_length=100)
    # comments_and_response = models.FileField(upload_to='', storage=None, max_length=100)
    # approved = models.FileField(upload_to='', storage=None, max_length=100)
    # as_built = models.FileField(upload_to='', storage=None, max_length=100)

    def __str__(self) -> str:
        return f"{self.division.prefix}{self.year}-{self.sequence}-{self.suffix}"

    class Meta():
        ordering = ["year", "sequence"]
        verbose_name = "Permit"
        verbose_name_plural = "Permits"

##########################################################################
""" The following should be moved to their own apps after the 
Building prototype is complete and "bug-free". """
##########################################################################

# class BLTag(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Business License Tag"
#         verbose_name_plural = "Business License Tags"
    
# class BLStatus(models.Model):  
#     """ Inherits Label, Description, Created, Modified """  
#     class Meta():
#         verbose_name = "BL Status"
#         verbose_name_plural = "BL Statuses"

# class BLType(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Business License Type"
#         verbose_name_plural = "Business License Types"
    
# class BLSubtype(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     type = models.ForeignKey(BLType, to_field="label", on_delete=models.PROTECT)
#     class Meta():
#         verbose_name = "Business License Subtype"
#         verbose_name_plural = "Business License Subtypes"

# class BL(Recordmodels.Model): # CRUD App
#     """ Inherits Label, Description, Created, Modified """
#     # Applicant, Inspection, Reviews, Fees, APN, Address, Owner, Received, Approved
#     # Over-writes label with specific formatting and formula.
#     type = models.ForeignKey(BLType, to_field="label", on_delete=models.PROTECT)
#     subtype = models.ForeignKey(BLSubtype, to_field="label", on_delete=models.PROTECT)
#     tags = models.ManyToManyField(BLTag)
#     status = models.ForeignKey(BLStatus, on_delete=models.PROTECT)

#     number = models.PositiveIntegerField(primary_key=True)
#     label = f"BL{timezone.now().strftime("%Y")}-{number}"
#     active = models.BooleanField()
#     expiration_date = models.DateField()
    
#     class Meta():
#         verbose_name = "Business License"
#         verbose_name_plural = "Business Licenses"

##########################################################################
""" Case Models """
##########################################################################

# class CETag(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Code Case Tag"
#         verbose_name_plural = "Code Case Tags"

# class CEStatus(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Code Case Status"
#         verbose_name_plural = "Code Case Statuses"

# class CEType(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Code Case Type"
#         verbose_name_plural = "Code Case Types"

# class CESubtype(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     type = models.ForeignKey(CEType, on_delete=models.PROTECT)
#     class Meta():
#         verbose_name = "Code Case Subtype"
#         verbose_name_plural = "Code Case Subtypes"

# class CE(Recordmodels.Model): # CRUD App
#     """ Inherits Label, Description, Created, Modified """
#     # Applicant, Inspection, Reviews, Fees, APN, Address, Owner, Received, Approved
#     # Over-writes label with specific formatting and formula.
#     type = models.ForeignKey(CEType, on_delete=models.PROTECT)
#     subtype = models.ForeignKey(CESubtype, on_delete=models.PROTECT)
#     tags = models.ManyToManyField(CETag)
#     status = models.ForeignKey(CEStatus, on_delete=models.PROTECT)

#     number = models.PositiveIntegerField(primary_key=True)
#     label = f"CE{timezone.now().strftime("%Y")}-{number}"
#     next_action_date = models.DateField()

#     # files_confidential = models.FileField(upload_to='', storage=None, max_length=100)
#     # files_public = models.FileField(upload_to='', storage=None, max_length=100)

#     class Meta():
#         verbose_name = "Code Case"
#         verbose_name_plural = "Code Cases"

##########################################################################
""" Public Works Models """
##########################################################################

# class PWTag(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Public Works Tag"
#         verbose_name_plural = "Public Works Tags"

# class PWStatus(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Public Works Status"
#         verbose_name_plural = "Public Works Statuses"

# class PWType(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Public Works Type"
#         verbose_name_plural = "Public Works Types"

# class PWSubtype(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     type = models.ForeignKey(PWType, on_delete=models.PROTECT)
#     class Meta():
#         verbose_name = "Public Works Subtype"
#         verbose_name_plural = "Public Works Subtypes"

# class PW(Recordmodels.Model): # CRUD App
#     """ Inherits Label, Description, Created, Modified """
#     # Applicant, Inspection, Reviews, Fees, APN, Address, Owner, Received, Approved
#     # Over-writes label with specific formatting and formula.
#     type = models.ForeignKey(PWType, on_delete=models.PROTECT)
#     subtype = models.ForeignKey(PWSubtype, on_delete=models.PROTECT)
#     tags = models.ManyToManyField(PWTag)
#     status = models.ForeignKey(PWStatus, on_delete=models.PROTECT)

#     number = models.PositiveIntegerField(primary_key=True)
#     label = f"PW{timezone.now().strftime("%Y")}-{number}"
#     next_action_date = models.DateField()

#     # files_confidential = models.FileField(upload_to='', storage=None, max_length=100)
#     # files_public = models.FileField(upload_to='', storage=None, max_length=100)

#     class Meta():
#         verbose_name = "Public Works Permits"
#         verbose_name_plural = "Public Works Permits"

##########################################################################
""" Planning Models """
##########################################################################

# class ZFTag(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Planning Tag"
#         verbose_name_plural = "Planning Tags"

# class ZFStatus(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Planning Status"
#         verbose_name_plural = "Planning Statuses"

# class ZFType(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     class Meta():
#         verbose_name = "Planning Type"
#         verbose_name_plural = "Planning Types"

# class ZFSubtype(models.Model): 
#     """ Inherits Label, Description, Created, Modified """
#     type = models.ForeignKey(ZFType, on_delete=models.PROTECT)
#     class Meta():
#         verbose_name = "Planning Subtype"
#         verbose_name_plural = "Planning Subtypes"

# class ZF(Recordmodels.Model): # CRUD App
#     """ Inherits Label, Description, Created, Modified """
#     # Applicant, Inspection, Reviews, Fees, APN, Address, Owner, Received, Approved
#     # Over-writes label with specific formatting and formula.
#     type = models.ForeignKey(ZFType, on_delete=models.PROTECT)
#     subtype = models.ForeignKey(ZFSubtype, on_delete=models.PROTECT)
#     tags = models.ManyToManyField(ZFTag)
#     status = models.ForeignKey(ZFStatus, on_delete=models.PROTECT)

#     number = models.PositiveIntegerField(primary_key=True)
#     label = f"ZF{timezone.now().strftime("%Y")}-{number}"

#     # files_confidential = models.FileField(upload_to='', storage=None, max_length=100)
#     # files_public = models.FileField(upload_to='', storage=None, max_length=100)

#     class Meta():
#         verbose_name = "Planning Permits"
#         verbose_name_plural = "Planning Permits"
        
##########################################################################
""" End File """
##########################################################################