from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

##########################################################################
""" Meta Models """
##########################################################################

class Division(models.Model): 
    prefix = models.CharField(max_length=5, unique=True) 
    division = models.CharField(max_length=30, unique=True)
    full_division = models.CharField(max_length=255, unique=True)
    year = models.CharField(max_length=55, default = timezone.now().strftime("%Y"))
    sequence = models.CharField(max_length = 12, default = "0000")

    class Meta:
        ordering = ["division"]
        verbose_name = "Division"
        verbose_name_plural = "Divisions"
    
    def __str__(self) -> str:
        return self.prefix
    
    def next(record_prefix, record_year):
        """ This function is mostly side-effects, and returns the next record number. """
        n = Division.objects.get(prefix=record_prefix)
        if n.year != record_year and n.prefix != "BL": 
            """ Annual Reset, except BL """
            n.year = record_year
            n.sequence = "0000"
        n.sequence = str(int(n.sequence) + 1)
        while len(n.sequence) < 4:
            """ Add leading zeros to the string. """
            n.sequence = f"0{n.sequence}"
        n.save()
        return {n.sequence}


class Tag(models.Model):      
    tag = models.CharField(max_length=100, blank = True, unique=True)
    policy = models.TextField(max_length=255, blank = True)

    def __str__(self) -> str:
        return self.tag   

    class Meta:
        ordering = ["tag"]
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Restriction(models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.PROTECT, blank = True, null = True)
    policy = models.CharField(max_length = 255, null = True, blank = True)

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
  

class Type(models.Model): 
    division = models.CharField(max_length=55, blank=True, null=True)
    prefix = models.CharField(max_length=7, blank=True, null=True)
    type = models.CharField(max_length=55, blank=True, null=True)
    policy = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=7, blank=True, null=True)
    # default_fees = models.ManyToManyField(FeeType, blank=True, null=True)
    # default_reviews = models.ManyToManyField(ReviewType, blank=True, null=True)
    # default_inspection = models.ManyToManyField(InspectionType, blank=True, null=True)

    def __str__(self) -> str:
        return self.type
    
    class Meta():
        ordering = ["type"]
        verbose_name = "Type"
        verbose_name_plural = "Types"


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

    
class Record(models.Model):
    number = models.CharField(max_length=55, unique = True)
    division = models.ForeignKey(Division, on_delete=models.PROTECT, null = True, blank = True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null = True, blank = True)

    description = models.CharField(max_length=55, blank=True)

    """ When creating a record search for address AND parcel and associate 
    with address whenever possible. Use dialog to encourage selection of
    an address when the applicant chooses a parce that has associated
    addresses. """
    location_type = ContentType() # either an address or apn
    location_id = models.PositiveSmallIntegerField(null=True, blank = True)
    location = GenericForeignKey(location_type, location_id)

    """ Use functions/forms to generate the following relationships 
    from their side as Foreign Keys to the Record. """
    # related = models.ManyToManyField("self", blank=True)
    # contacts = models.ForeignKey(Contact, on_delete=models.PROTECT, blank=True)
    # reviews = models.ManyToManyField(ReviewType, through=Review, blank=True)
    # inspections = models.ManyToManyField(InspectionType, through=Inspection, blank=True)
    # fees = models.ManyToManyField(FeeType, through=Fee, blank=True)
    
    def set_number(self):
        year = timezone.now().strftime("%Y")
        sequence = Division.next(self.prefix, year)
        return f"{self.prefix}{year}-{sequence}-{self.suffix}"

    class Meta():
        ordering = ["number"]
        verbose_name = "Record"
        verbose_name_plural = "Records"

##########################################################################
""" End File """
##########################################################################