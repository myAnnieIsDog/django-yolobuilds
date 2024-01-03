##########################################################################
""" Fee Type Models """
##########################################################################
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

def yaml_fees(all_models):
    from general.models import yaml_backup
    yaml_backup(all_models)


# ##########################################################################
# """ Fund Model """
# ##########################################################################
# class Fund(models.Model):
#     """ General, Building, and Roads. """


#     def __str__(self) -> str:
#         return self.fund_label
    
#     class Meta():
#         verbose_name = "Budget Units and Funds"
#         verbose_name_plural = "Budget Units and Funds"

#     def bak(self):
#         yaml_fees([self])


##########################################################################
""" Fiscal Accounts Model """
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
        verbose_name = "Budget Unit"
        verbose_name_plural = "Budget Units"


# ##########################################################################
# """ User Interface Group """
# ##########################################################################
# class UIGroup(models.Model):
#     # fee = models.ForeignKey(
#     #     "FeeType", 
#     #     on_delete=models.PROTECT,
#     #     null=True
#     # )
#     group = models.CharField(
#         max_length=55,
#         unique=True,
#     )
#     def __str__(self) -> str:
#         return self.group 
    
#     class Meta():
#         verbose_name = "Fee Group"
#         verbose_name_plural = "Fee Groups"


##########################################################################
""" Fee Schedule Model """
##########################################################################
class FeeType(models.Model): 
    
    fee_account = models.ManyToManyField(Account)

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
""" All Models """
##########################################################################
all_models = {
    Account,
    FeeType,
}
##########################################################################
""" END FILE """
##########################################################################