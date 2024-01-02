##########################################################################
""" Review Models.  See permits.models for ReviewType, which was 
placed there to prevent a circular reference to the Permit model. """
##########################################################################
from django.db import models
from permits.models import ReviewType

class ReviewStatus(models.Model): 
    """ Inherits Label, Description, Created, Modified """
    class Meta():
        verbose_name = "Review Status Option"
        verbose_name_plural = "Review Status Options"

class Review(models.Model):
    """ Inherits Label, Description, Created, Modified """
    type = models.ForeignKey(ReviewType, on_delete=models.PROTECT)   
    status = models.ForeignKey(ReviewStatus, on_delete=models.PROTECT)  
   
    # Fee Study
    staff_time_allotted = models.DecimalField(max_digits=7, decimal_places=1)
    staff_time_actual = models.DecimalField(max_digits=7, decimal_places=1)

class ReviewCycle(models.Model):
    """ Inherits Label, Description, Created, Modified """
    review = models.ForeignKey(Review, on_delete=models.PROTECT)
    cycle = models.PositiveSmallIntegerField(default=1)
    status = models.ForeignKey(ReviewStatus, on_delete=models.PROTECT, default="Under Review")
    reviewer = models.CharField(max_length=100, null=True)
    completed_date = models.DateTimeField(null=True)

    staff_time_actual = models.DecimalField(max_digits=7, decimal_places=1)
    days_until_due = models.DurationField(null=True)
    age = models.DurationField(null=True)
    due = models.DateTimeField(null=True)
    days_allotted = models.DurationField(null=True)
    sent = models.DateTimeField(null=True)

##########################################################################
""" All Models """
##########################################################################
all_models = (
    ReviewType,
    ReviewStatus,
    Review,
    ReviewCycle,
)
##########################################################################
""" End File """
##########################################################################