from django.db import models

##########################################################################
""" Base Models """
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
class Number(models.Model):
    title = models.CharField(max_length = 55)
    prefix = models.CharField(max_length=2)
    year = models.DateTimeField(default=timezone.now().strftime("%Y"))
    number = models.CharField(max_length=4, default="0000")

    def __str__(self) -> str:
        return self.series  
    # BL, BP, CE, PW, ZF, Receipt, etc.

    def next(series): # <- series title
        n = Number.objects.get(series_title=series)
        n.year = timezone.now().strftime("%Y")
        n.sequence = str(int(n.sequence) + 1)
        while len(n.sequence) < 4:
            n.sequence = f"0{n.sequence}"
        return f"{n.series}{n.year}-{n.sequence}"
    
    class Meta:
        ordering = ["prefix", "year", "number"]
        verbose_name = "Number"
        verbose_name_plural = "Numbers"

##########################################################################
""" Restrictions """
##########################################################################
class Tag(models.Model):      
    tag = models.CharField(max_length=100, unique=True)
    policy = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.tag   

    class Meta:
        ordering = ["tag"]
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Restriction(models.Model):
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
        ordering = ["tag"]
        verbose_name = "Restriction"
        verbose_name_plural = "Restrictions"

  
##########################################################################
""" Permit Options """
#########################################################################
class Status(models.Model): 
    status = models.CharField(max_length=30, unique=True)
    policy = models.CharField(max_length=255)
    build = models.BooleanField(default=False)
    occupy = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.status
    
    class Meta:
        ordering = ["status"]
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Form(models.Model):
    form = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.form
    
    class Meta:
        ordering = ["form"]
        verbose_name = "Form"
        verbose_name_plural = "Forms"


class Question(models.Model):
    question = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.question
    
    class Meta:
        ordering = ["question"]
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Type(models.Model): 
    type = models.CharField(max_length=255, unique=True)
    policy = models.CharField(max_length=255)
    suffix = models.CharField(max_length=7, default="Ex-R", unique=True)
    default_fees = models.ManyToManyField("fees.FeeType", blank=True)
    default_reviews = models.ManyToManyField("reviews.ReviewType", blank=True)
    default_inspection = models.ManyToManyField("inspections.InspectionType", blank=True)
    default_forms = models.ManyToManyField(Form, blank=True)
    default_app_questions = models.ManyToManyField(Question, blank=True)

    def __str__(self) -> str:
        return self.type
    
    class Meta():
        ordering = ["type"]
        verbose_name = "Type"
        verbose_name_plural = "Types"

    
##########################################################################
""" Generic Records """
##########################################################################
class Record(models.Model):
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    number = models.CharField(max_length=55, blank=True)
    description = models.TextField(max_length=55)
    details = models.TextField(max_length=255)
    
    scope = models.ManyToManyField(Type, blank=True)
    apn = models.ManyToManyField(Parcel, blank=True)
    address = models.ManyToManyField(SiteAddress, blank=True)
    related = models.ManyToManyField("self", blank=True)
    contacts = models.ManyToManyField(
        Profile, through="Contact", blank=True)
    app_questions = models.ManyToManyField(Question, blank=True)
    forms = models.ManyToManyField("form", blank=True)
    reviews = models.ManyToManyField(
        "reviews.ReviewType", through="reviews.Review", blank=True)
    inspections = models.ManyToManyField(
        "inspections.InspectionType", through="inspections.Inspection", blank=True)
    fees = models.ManyToManyField(
        "fees.FeeType", through="fees.Fee", blank=True)

    def __str__(self) -> str:
        return f"{self.number}-{self.type.suffix}-{self.type.type}"
    
    def set_number(self):
        self.number = "BP24-0001"  # Replace with function.

    class Meta():
        ordering = ["number"]
        verbose_name = "Record"
        verbose_name_plural = "Records"


class ContactType(models.Model):
    role = models.CharField(max_length=55)
    description = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.role

    class Meta():
        ordering = ["description"]
        verbose_name = "Contact Type"
        verbose_name_plural = "Contacts Types"


class Contact(models.Model):
    record = models.ForeignKey(Record, on_delete=models.PROTECT)
    contact = models.ForeignKey(Profile, on_delete=models.PROTECT)
    contact_type = models.ForeignKey(ContactType, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.contact} is the {self.role} on {self.record}."
    
    class Meta():
        ordering = ["contact"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


##########################################################################
""" All Models """
##########################################################################
"""This list only includes models that are in their stable form."""
all_models = (
    Number,
    Tag,
    Restriction,
    Form,
    Question,
    Status,
    Type,
    Record,
    ContactType,
    Contact,
)
##########################################################################
""" End File """
##########################################################################
