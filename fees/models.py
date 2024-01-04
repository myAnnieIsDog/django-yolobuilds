##########################################################################
""" Fee Type Models """
##########################################################################
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
import requests

from profiles.models import Profile


def yaml_fees(model_list: list) -> bool:
    from scripts.bak_yaml import yaml_backup
    return yaml_backup(model_list)


##########################################################################
""" Accounts Model """
##########################################################################
class Account(models.Model): 

    fund = models.CharField(
        max_length=4)
    fund_label = models.CharField(
        max_length=55)
    share = models.DecimalField(
        max_digits=3, decimal_places=2, default=1.00)
    unit = models.CharField(
        max_length=4)
    unit_label = models.CharField(
        max_length=55)
    unit_description = models.CharField(
        max_length=255)
    cost_center = models.CharField(
        max_length=6)
    gl_account = models.CharField(
        max_length=6, unique=True)
    cams = models.CharField(
        max_length=9)
    infor_activity = models.CharField(
        max_length=7)
    infor_account = models.CharField(
        max_length=5)
    ledger = models.CharField(
        max_length=20)
    def __str__(self) -> str:
        return self.unit_label
    
    class Meta():
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


##########################################################################
""" Fee Types Model """
##########################################################################
class FeeType(models.Model): 
    
    fee_account = models.ForeignKey(Account, on_delete=models.PROTECT)

    fee_group = models.CharField(
        max_length=255, 
        unique=True,
    )
    fee_type = models.CharField(
        max_length=255, 
        unique=True,
    )
    policy = models.TextField(
        max_length=1000, 
        null=True, 
        blank=True,
    )
    authorization = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
    )
    adopted = models.DateField(
        null=True, 
        blank=True,
    )
    revised = models.DateField(
        null=True, 
        blank=True,
    )
    expires = models.DateField(
        null=True, 
        blank=True,
    )
    tier_base_qty = models.DecimalField(
        max_digits=15, 
        decimal_places=0, 
        default=0, 
    )
    tier_base_fee = models.FloatField(
        default=0,
    )
    rate = models.FloatField(
        default=5000000,
    )
    units = models.CharField(
        max_length=255, 
        default="each",
    )
    rate_check = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
    ) 
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.fee_type 
    
    class Meta():
        ordering = ["fee_type"]
        verbose_name = "Fee Type"
        verbose_name_plural = "Fee Types"


##########################################################################
""" Model for fees applied to a record."""
##########################################################################
class Fee(models.Model):
    # Attach the fee to a record of various types (permit, license, case)
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


##########################################################################
""" Payment Model. """
##########################################################################
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


    def converge(
        ssl_pin="123",
        ssl_transaction_type="ccsale",
        ssl_amount="0.10", 
        merchant_id="000062",
        merchant_user_id="sdoolittle",
        merchant_pin="tbd",
        demo="", 
        **kwargs
    ):
        params = {
            "ssl_pin": ssl_pin,
            "ssl_transaction_type": ssl_transaction_type,
            "ssl_amount": ssl_amount, 
            "merchant_id": merchant_id,
            "merchant_user_id": merchant_user_id,
            "merchant_pin": merchant_pin,
        }
        demo = "demo." # comment-out for production url's to use the default empty string.
        token_url = (f"https://api.{demo}convergepay.com/hosted-payments/transaction_token")
        response = requests.post(token_url, params)  
        print(response)
        response.raise_for_status()
        if response.status_code == 200:
            header = (f"Location: https://api.{demo}convergepay.com/hosted-payments?ssl_txn_auth_token=$sessiontoken")
            return requests.post(header)
        else:
            return f"HTTP Status: {response.status_code}. {response}"

    # print(converge(ssl_amount = 0.50))

    
##########################################################################
""" All Models """
##########################################################################
all_models = (
    Account,
    FeeType,
    Fee,
    ClaritiFee,
    TrakitFee,
    PaymentMethod,
    Payment,
)
##########################################################################
""" END FILE """
##########################################################################