from django.contrib import admin
from .models import (Account, FeeType, Fee, 
                     TrakitFee, ClaritiFee, PaymentMethod, Payment)


##########################################################################
""" Fee Admin """
##########################################################################

admin.site.site_title = 'Fee Schedule and Configuration'

class FeeTypeInline(admin.TabularInline):
    model = FeeType
    extra = 1
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "fund_label", 
        "unit_label",
        "cost_center",
    ]
    ordering = ["fund_label","unit_label"]
    list_display_links = [
        "fund_label", 
        "unit_label",
        "cost_center",
    ]
    list_filter = ["fund_label"]
    actions_on_bottom = True
    inlines = [FeeTypeInline]
    name = "Fiscal Accounts"



@admin.register(FeeType)
class FeeTypeAdmin(admin.ModelAdmin):
    list_display = [
        "fee_account",
        "fee_group",
        "fee_name",  
        "tier_base_qty", 
        "tier_base_fee",
        "rate", 
        "units", 
        "rate_check", 
    ]
    ordering = [
        "fee_group", 
        "fee_name", 
    ]
    list_display_links = [
        # "fee_account",
        "fee_group", 
        "fee_name", 
        # "tier_base_qty", 
        # "tier_base_fee",
        # "rate", 
        # "units", 
        "rate_check", 
    ]
    list_editable = [
        "fee_account",
        # "fee_group",
        # "fee_type", 
        "tier_base_qty", 
        "tier_base_fee",
        "rate", 
        "units",
        #"rate_check", 
    ]
    list_filter = [
        # "fee_account",
        "fee_group",
        "active",
        "deleted",
    ]
    name = "Fee Types"


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    pass

@admin.register(TrakitFee)
class TrakitFeeAdmin(admin.ModelAdmin):
    name = "TRAKiT Fees"

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    name = "Payment Methods"
    list_display = ["method", "policy"]
    list_display_links = ["method", "policy"]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass

@admin.register(ClaritiFee)
class ClaritiFeeAdmin(admin.ModelAdmin):
    pass

##########################################################################
""" End File """
##########################################################################