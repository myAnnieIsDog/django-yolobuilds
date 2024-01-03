from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from fees.models import FeeType
from profiles.models import Profile

##########################################################################
""" Payment Models. These are the fees related to a specific 
permit/license. See fees.models for a schedule of fee types."""
##########################################################################

class Fee(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    fee_type = models.ForeignKey(FeeType, on_delete=models.PROTECT)
    qty = models.DecimalField(max_digits=20, decimal_places=7, default=1.0)
    rate = models.DecimalField(max_digits=15, decimal_places=2, default=1.00)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=1.00)

    paid_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    paid_date = models.DateTimeField(null=True, blank=True)
    receipt_number = models.CharField(max_length=25, null=True, blank=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=1000000)
    fully_paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    notes = models.TextField(max_length=255)


class ClaritiFee(Fee):
    pass


class TrakitFee(Fee):
    trakit_fee_code = models.CharField(max_length=255, null=True, blank=True)
    tech = models.CharField(max_length=255, null=True, blank=True)
    trakit_description = models.CharField(max_length=255, null=True, blank=True)
    trakit_formula = models.CharField(max_length=255, null=True, blank=True)
    trakit_id = models.CharField(max_length=255, null=True, blank=True)


class PaymentMethod(models.Model):
    method = models.CharField(max_length=55, unique=True)
    policy = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.method

    class Meta:
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"


class Payment(models.Model):
    fees = models.ManyToManyField(Fee)
    method = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    paid_by = models.OneToOneField(Profile, on_delete=models.CASCADE)
    check_number = models.CharField(max_length=255, null=True, blank=True)
    receipt_number = models.PositiveSmallIntegerField(null=True)
    collected_by = models.ForeignKey(User, on_delete=models.PROTECT)
    deposit = models.BooleanField(default=False)
    refund = models.BooleanField(default=False)

    def pay_now():
        # Process the transaction. FUTURE: integrate with Elavon/Converge.
        # Generate a pdf receipt, save it to the payments directory, link 
        # the file to the related fee records, and display it to the user 
        # for printing. 
        pass

##########################################################################
""" All Models """
##########################################################################
all_models = (
    Fee,
    ClaritiFee,
    TrakitFee,
    PaymentMethod,
    Cart,
    Payment,
)
##########################################################################
""" End File """
##########################################################################