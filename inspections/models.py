from django.db import models
from permits.models import Division
from profiles.models import User

##########################################################################
""" Inspection Models.  See permits.models for InspectionType, which was 
placed there to prevent a circular reference to the Permit model. """
##########################################################################

class InspectionType(models.Model): 
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    inspection_type = models.CharField(max_length=30)
    default_inspector = models.ForeignKey(User, on_delete=models.PROTECT)
    duration_hours = models.DecimalField(
        max_digits=3, decimal_places=1, default=0.3)
    trip_factor = models.DecimalField(
        max_digits=7, decimal_places=2, default=1.20)

    prerequisite = models.ManyToManyField("self", blank=True)
    inspection_checklist = models.TextField(blank=True)
    add_next = models.ManyToManyField("self", blank=True)
    
    
    def __str__(self) -> str:
        return self.type

    class Meta():
        verbose_name = "Inspection Type"
        verbose_name_plural = "Inspection Types"


class InspectionResult(models.Model): 
    """ Inherits Label, Description, Created, Modified """
    class Meta():
        verbose_name = "Inspection Result Option"
        verbose_name_plural = "Inspection Result Options"

class Inspection(models.Model):
    """ Inherits Label, Description, Created, Modified """

    # permit = models.ForeignKey(Permit, on_delete=models.DO_NOTHING, null=True)
    # permit_type, permit_subtype, permit_description, permit_status
    type = models.ForeignKey(InspectionType, on_delete=models.PROTECT)   
    status = models.ForeignKey(InspectionResult, on_delete=models.PROTECT) 

    # Fee Study
    staff_time_allotted = models.DecimalField(max_digits=7, decimal_places=1)
    staff_time_actual = models.DecimalField(max_digits=7, decimal_places=1)     

class InspectionTrip(models.Model):
    """ Inherits Label, Description, Created, Modified """
    inspection = models.ForeignKey(Inspection, on_delete=models.PROTECT)   
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

##########################################################################
""" All Models """
##########################################################################
all_models = (
    InspectionType,
    InspectionResult,
    Inspection,
    InspectionTrip,
)
##########################################################################
""" End File """
##########################################################################