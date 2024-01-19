from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from django.views.generic.edit import CreateView
from typing import Any, Callable

from .models import Demolition

##########################################################################
""" Demolition """
##########################################################################


class DemolitionCreateView(CreateView):
    def get():
        model = Demolition
        fields = [
            'number_of_structures',
            'demolition_area',
            'description',
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

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.receive()
        return super().post(request, *args, **kwargs)
    # def post(self):
    #     

    


