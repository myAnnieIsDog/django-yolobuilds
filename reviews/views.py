from typing import Any
from django.db.models.base import Model as Model
from django.views.generic import ListView, DetailView 

from .models import Review, ReviewCycle

##########################################################################
""" Review Views """
##########################################################################
class ReviewList(ListView):
    model = Review

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["reviews"] = ReviewCycle.objects.all().filter(status="Under Review")
        return context


class ReviewDetail(DetailView):
    model = Review

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["cycles"] = ReviewCycle.objects.all().filter(review=self.kwargs["pk"])
        return context

##########################################################################
""" End File """
##########################################################################