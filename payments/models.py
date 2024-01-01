from django.db import models
from fees.models import FeeType
from profiles.models import Profile

##########################################################################
""" Payment Models. These are the fees related to a specific 
permit/license. See fees.models for a schedule of fee types."""
##########################################################################

class PaymentMethods(models.Model):
    method = models.CharField(max_length=55, unique=True)

    class Meta:
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"


class Fee(models.Model):
    fee_type = models.ForeignKey(FeeType, on_delete=models.PROTECT)
    qty = models.DecimalField(max_digits=20, decimal_places=7, default=1.0)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=1.00)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=1000000)

    # Concatenate into the description field:
    trakit_code = models.CharField(max_length=256, null=True, blank=True)
    tech = models.CharField(max_length=256, null=True, blank=True)
    trakit_description = models.CharField(max_length=256, null=True, blank=True)
    trakit_formula = models.CharField(max_length=256, null=True, blank=True)
    trakit_id = models.CharField(max_length=256, null=True, blank=True)


class Cart(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="cart_user")
    fees = models.ManyToManyField(Fee)
    method = models.ForeignKey(PaymentMethods, on_delete=models.PROTECT)


class Payment(models.Model):
    account = models.OneToOneField(Profile, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    fees = models.ManyToManyField(Fee)
    date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    paid_by = models.CharField(max_length=256, null=True, blank=True)
    method = models.CharField(max_length=256, null=True, blank=True)
    check_number = models.CharField(max_length=256, null=True, blank=True)
    ib_number = models.CharField(max_length=256, null=True, blank=True)
    receipt_number = models.PositiveSmallIntegerField(null=True)
    collected_by = models.CharField(max_length=256, null=True, blank=True)

    def pay_now():
        # Process the transaction. FUTURE: integrate with Elavon/Converge.
        # Generate a pdf receipt, save it to the payments directory, link 
        # the file to the related fee records, and display it to the user 
        # for printing. 
        pass

##########################################################################
""" End File """
##########################################################################