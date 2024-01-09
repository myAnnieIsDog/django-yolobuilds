from django.contrib import admin
from .models import (Account, FeeType, Fee, 
                     TrakitFee, PaymentMethod, Payment)


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
        "share",
    ]
    ordering = ["fund_label","unit_label"]
    list_display_links = [
        "fund_label", 
        "unit_label",
        "share",
    ]
    actions_on_bottom = True
    inlines = [FeeTypeInline]
    name = "Fiscal Accounts"



@admin.register(FeeType)
class FeeTypeAdmin(admin.ModelAdmin):
    list_display = [
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
        "fee_group", 
        "fee_name", 
        # "tier_base_qty", 
        # "tier_base_fee",
        # "rate", 
        # "units", 
        "rate_check", 
    ]
    list_editable = [
        # "fee_group",
        # "fee_type", 
        "tier_base_qty", 
        "tier_base_fee",
        "rate", 
        "units",
        #"rate_check", 
    ]
    list_filter = [
        "fee_group",
        "active",
        "deleted",
    ]
    name = "Fee Types"


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    pass

@admin.register(TrakitFee)
class FeeAdmin(admin.ModelAdmin):
    name = "TRAKiT Fees"

@admin.register(PaymentMethod)
class FeeAdmin(admin.ModelAdmin):
    name = "Payment Methods"

@admin.register(Payment)
class FeeAdmin(admin.ModelAdmin):
    pass

##########################################################################
""" End File """
##########################################################################