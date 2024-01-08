from django.views.generic import base, detail, list, edit, dates
from .models import FeeType
from .models import (Account, FeeType, Fee, 
                     TrakitFee, PaymentMethod, Payment)

class FiscalDetailView(detail.DetailView):
    template_name = "layout_form.html"
    model = FeeType
    fields = "__all__"
    extra_context = {
        "heading": "Fee Types", 
        "intro": "This is a list of all of the fees charged by Yolo Builds."
    }