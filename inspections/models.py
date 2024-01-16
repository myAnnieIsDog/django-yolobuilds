from django.db import models
from records.models import Record
from profiles.models import User

##########################################################################
""" Inspection Models """
##########################################################################

class InspectionGroup(models.Model):
    group = models.CharField(max_length=55, blank=True)

    def __str__(self) -> str:
        return self.group

    class Meta():
        ordering = ["group"]
        verbose_name = "Inspection Group"
        verbose_name_plural = "Inspection Groups"

class InspectionType(models.Model): 
    insp_group = models.ForeignKey(
        InspectionGroup, on_delete=models.PROTECT, null=True, blank=True)
    inspection_type = models.CharField(
        max_length=255)
    default_inspector = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    duration_hours = models.DecimalField(
        max_digits=3, decimal_places=1, default=0.3)
    trip_factor = models.DecimalField(
        max_digits=7, decimal_places=2, default=1.20)
    inspection_checklist = models.TextField(blank=True)   
    
    def __str__(self) -> str:
        return self.inspection_type

    class Meta():
        ordering = ["insp_group", "inspection_type"]
        verbose_name = "Inspection Type"
        verbose_name_plural = "Inspection Types"


class InspectionResult(models.Model): 
    result = models.CharField(max_length=55, unique=True)
    requirements = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.result

    class Meta():
        ordering = ["result"]
        verbose_name = "Inspection Result Option"
        verbose_name_plural = "Inspection Result Options"

class Inspection(models.Model):
    """ Inherits Label, Description, Created, Modified """

    permit = models.ForeignKey(Record, on_delete=models.DO_NOTHING, null=True)
    # permit_type, permit_subtype, permit_description, permit_status
    type = models.ForeignKey(InspectionType, on_delete=models.PROTECT)   
    status = models.ForeignKey(InspectionResult, on_delete=models.PROTECT) 

    # Fee Study
    staff_time_allotted = models.DecimalField(max_digits=7, decimal_places=1)
    staff_time_actual = models.DecimalField(max_digits=7, decimal_places=1)     

    def __str__(self) -> str:
        return self.type
    
    class Meta():
        ordering = ["type"]
        verbose_name = "Inspection"
        verbose_name_plural = "Inspections"

class InspectionTrip(models.Model):
    """ Inherits Label, Description, Created, Modified """
    inspection = models.ForeignKey(Inspection, on_delete=models.PROTECT)  
    trip_number = models.PositiveSmallIntegerField(default=0) 
    result = models.ForeignKey(InspectionResult, on_delete=models.PROTECT)   
    resulted = models.DateTimeField(null=True)
    inspector = models.CharField(max_length=100, null=True, blank=True)

    time_allotted = models.DecimalField(max_digits=7, decimal_places=1)
    time_actual = models.DecimalField(max_digits=7, decimal_places=1)
    time_delta = models.DecimalField(max_digits=7, decimal_places=1)

    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()

    requested_by = models.CharField(max_length=100, null=True, blank=True)
    requested_date = models.DateField()
    requested_notes = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        ordering = ["inspection", "trip_number"]
        verbose_name = "Inspection Trip"
        verbose_name_plural = "Inspection Trips"
##########################################################################
""" All Models """
##########################################################################
all_models = (
    InspectionGroup,
    InspectionType,
    InspectionResult,
    Inspection,
    InspectionTrip,
)
##########################################################################
""" End File """
##########################################################################