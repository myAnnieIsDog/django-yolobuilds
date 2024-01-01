from django.contrib import admin
from .models import Fund, BudgetUnit, FeeType, UIGroup, UnitPortion


##########################################################################
""" Fee Admin """
##########################################################################

admin.site.site_title = 'Fee Schedule and Configuration'

class BudgetUnitInline(admin.TabularInline):
    model = BudgetUnit
    extra = 0
    list_editable = [
        "unit_label", 
        "unit", 
        "unit_description",
    ]   
@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = [
        "fund_label", 
        "fund_id", 
        "fund_description",
    ]
    ordering = ["fund_label"]
    list_display_links = [
        "fund_label", 
        "fund_id", 
        "fund_description",
    ]
    actions_on_bottom = True
    inlines = [BudgetUnitInline]
    name = "Funds and Budget Units"


@admin.register(UnitPortion)
class UnitPortionAdmin(admin.ModelAdmin):
    list_display = [
        "fee",
        "unit", 
        "share", 
    ]
    list_editable = [
        "unit", 
        "share", 
    ]
    ordering = ["fee"]


@admin.register(UIGroup)
class UIGroupAdmin(admin.ModelAdmin):
    list_display = ["id","group"]
    list_editable = ["group"]
    ordering = ["group"]

class UnitPortionInline(admin.StackedInline):
    model = UnitPortion
    extra = 0
    # list_editable = [
    #     "unit", 
    #     "share",
    # ]   

@admin.register(FeeType)
class FeeTypeAdmin(admin.ModelAdmin):
    list_display = [
        "fee_group",
        "fee_type", 
        "tier_base_qty", 
        "tier_base_fee",
        "rate", 
        "units", 
        "rate_check", 
    ]
    ordering = [
        "fee_type", 
    ]
    list_display_links = [
        # "fee_group",
        "fee_type", 
        # "tier_base_qty", 
        # "tier_base_fee",
        # "rate", 
        # "units", 
        # "rate_check", 
    ]
    list_editable = [
        # "fee_group",
        # "fee_type", 
        "tier_base_qty", 
        "tier_base_fee",
        "rate", 
        "units",
        "rate_check", 
    ]
    list_filter = [
        "fee_group",
        "active",
        "deleted",
    ]
    inlines = [UnitPortionInline]

##########################################################################
""" End File """
##########################################################################