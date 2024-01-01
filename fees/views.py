from crispy_forms.helper import FormHelper
from django.views.generic import base, detail, list, edit, dates
from .models import FeeType


class FiscalDetailView(detail.DetailView):
    template_name = "layout_form.html"
    model = FeeType
    fields = "__all__"
    extra_context = {
        "heading": "Fee Types", 
        "intro": "This is a list of all of the fees charged by Yolo Builds."
    }
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
