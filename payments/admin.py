from django.contrib import admin
from .models import PaymentMethods, Fee, Cart, Payment

##########################################################################
""" Payment Admin """
##########################################################################

@admin.register(PaymentMethods)
class PaymentMethodsAdmin(admin.ModelAdmin):
    pass

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass

##########################################################################
""" End File """
##########################################################################