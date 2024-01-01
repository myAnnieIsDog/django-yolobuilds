##########################################################################
""" Fee Type Models """
##########################################################################
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


##########################################################################
""" Fund Model """
##########################################################################
class Fund(models.Model):
    """ General, Building, and Roads. """

    fund_label = models.CharField(
        max_length=30, 
        unique=True,
    ) 
    fund_id = models.CharField(
        max_length=4, 
        unique=True,
    )
    fund_description = models.CharField(
        max_length=4, 
        unique=True,
    )
    def __str__(self) -> str:
        return self.fund_label
    
    class Meta():
        verbose_name = "Budget Units and Funds"
        verbose_name_plural = "Budget Units and Funds"


##########################################################################
""" Budget Unit Model """
##########################################################################
class BudgetUnit(models.Model): 
    """ Each fund has 4-6 budget units. """
    unit_fund = models.ForeignKey(
        Fund, 
        on_delete=models.PROTECT, 
        null=True,
    )
    unit_label = models.CharField(
        max_length=40, 
        unique=True,
    )
    unit = models.CharField(
        max_length=6, 
        unique=True,
    )
    unit_description = models.CharField(
        max_length=100, 
        unique=True,
    )
    def __str__(self) -> str:
        return self.unit_label 
    
    class Meta():
        verbose_name = "Budget Unit"
        verbose_name_plural = "Budget Units"


##########################################################################
""" User Interface Group """
##########################################################################
class UIGroup(models.Model):
    # fee = models.ForeignKey(
    #     "FeeType", 
    #     on_delete=models.PROTECT,
    #     null=True
    # )
    group = models.CharField(
        max_length=55,
        unique=True,
    )
    def __str__(self) -> str:
        return self.group 
    
    class Meta():
        verbose_name = "Fee Group"
        verbose_name_plural = "Fee Groups"


##########################################################################
""" Fee Schedule Model """
##########################################################################
class FeeType(models.Model): 
    unit = models.ManyToManyField(
        BudgetUnit,
        through="UnitPortion"
    )
    fee_group = models.ForeignKey(
        UIGroup,
        on_delete=models.PROTECT,
        null=True,
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
""" Unit Portion Model """
##########################################################################
class UnitPortion(models.Model):
    fee = models.ForeignKey(
        FeeType,
        on_delete=models.DO_NOTHING, 
        null=True, 
        blank=True,
    )
    unit = models.ForeignKey(
        BudgetUnit,
        on_delete=models.DO_NOTHING, 
        null=True, 
        blank=True,
    )
    share = models.DecimalField(
        max_digits=3, 
        decimal_places=2, 
        default=1.00,
        validators=[
            MinValueValidator(0.00), 
            MaxValueValidator(1.00),
        ], 
    )
    def __str__(self) -> str:
        return self.unit.unit 
    
    class Meta():
        verbose_name = "Fee to Budget Unit Portions"
        verbose_name_plural = "Fee to Budget Unit Portions"


##########################################################################
""" END FILE """
##########################################################################