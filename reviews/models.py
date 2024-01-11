##########################################################################
""" Review Models.  See permits.models for ReviewType, which was 
placed there to prevent a circular reference to the Permit model. """
##########################################################################
from django.db import models
from fees.models import FeeType
from permits.models import Division, Permit
from profiles.models import User


class ReviewType(models.Model): 
    review_division = models.ForeignKey(
        Division, on_delete=models.PROTECT, related_name="+", 
        null=True, blank=True)
    default_reviewer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+", 
        null=True, blank=True)
    review_type = models.CharField(max_length=30)
    days_cycle1 = models.PositiveSmallIntegerField(default=15)
    days_cycle2 = models.PositiveSmallIntegerField(default=5)
    review_fees = models.ManyToManyField(
        FeeType, related_name="+", blank=True)
    prerequisite = models.ManyToManyField("self", blank=True)
    review_checklist = models.TextField("Review Checklist", blank=True)
    add_next = models.ManyToManyField("self", blank=True)

    def __str__(self) -> str:
        return self.review_type

    class Meta():
        verbose_name = "Review Type"
        verbose_name_plural = "Review Types"


class ReviewStatus(models.Model): 
    status = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.status

    class Meta():
        verbose_name = "Review Status Option"
        verbose_name_plural = "Review Status Options"


class Review(models.Model):
    permit = models.ForeignKey(Permit, on_delete=models.PROTECT) 
    type = models.ForeignKey(ReviewType, on_delete=models.PROTECT)   
    status = models.ForeignKey(ReviewStatus, on_delete=models.PROTECT)
    coa = models.TextField("Conditions of Approval", max_length=255)  
   
    # Fee Study
    staff_time_allotted = models.DecimalField(max_digits=7, decimal_places=1)
    staff_time_actual = models.DecimalField(max_digits=7, decimal_places=1)

    def __str__(self) -> str:
        return f"{self.permit.number} {self.type.review_type}"


class CycleResult(models.Model):
    result = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    causes_review_status = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.result
    
    class Meta():
        verbose_name = "Cycle Result Option"
        verbose_name_plural = "Cycle Result Options"


class ReviewCycle(models.Model):
    """ Inherits Label, Description, Created, Modified """
    # Fields for ReviewCycle.objects.filter(parent_review=review)
    review = models.ForeignKey(Review, on_delete=models.PROTECT, related_name="cycle")
    
    # Public fields
    cycle = models.PositiveSmallIntegerField(default=1)
    result = models.ForeignKey(CycleResult, on_delete=models.PROTECT, default="In Progress")
    reviewer = models.CharField(max_length=100, null=True)
    completed_date = models.DateTimeField(null=True)
    due = models.DateTimeField(null=True)
    sent = models.DateTimeField(null=True)
    notes = models.TextField(max_length=255)

    staff_time_actual = models.DecimalField(max_digits=7, decimal_places=1)
    days_until_due = models.DurationField(null=True)
    age = models.DurationField(null=True)
    
    days_allotted = models.DurationField(null=True)

    def __str__(self) -> str:
        return f"{self.cycle}"
    
    class Meta():
        verbose_name = "Review Cycle"
        verbose_name_plural = "Review Cycles"


##########################################################################
""" All Models """
##########################################################################
all_models = (
    ReviewType,
    ReviewStatus,
    Review,
    CycleResult,
    ReviewCycle,
)
##########################################################################
""" End File """
##########################################################################