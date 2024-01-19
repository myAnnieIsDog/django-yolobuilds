from django.forms import ModelForm
from .models import Demolition

class DemolitionForm(ModelForm):
     class Meta:
         model = Demolition
         fields = [
            'description', 
            'number_of_structures',
            'demolition_area',
            'address', 
            'apn',
            'related',
            'contacts',
            'valuation',
            'owner_builder_form',
            'owner_rep_form',
            'CSLB_Forms',
            'employee_authorization',
        ]
