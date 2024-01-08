from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView 

from django.shortcuts import render
from django.forms import modelformset_factory, BaseModelFormSet
from .models import ReviewType, ReviewStatus, Review, ReviewCycle


class ReviewList(ListView):
    model = Review

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()


class ReviewDetail(DetailView):
    model = Review
    


    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     cycles = ReviewCycle.objects.all().filter(review=self.pk)
    #     context["cycles"] = cycles
    #     return context

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["cycles"] = ReviewCycle.objects.all().filter(review=self.kwargs["pk"])
        return context
    
 
    
    



##########################################################################
""" Review Views """
##########################################################################

# class BaseReviewFormSet(BaseModelFormSet):
#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.queryset = Review.objects.filter(permit=parent)

# def manage_permit_reviews(request, parent):
#     ReviewFormSet = modelformset_factory(
#         Review,
#         fields=["__all__"],
#         # exclude=["__all__"],
#         formset=BaseReviewFormSet(permit=parent)
#         # widgets = {"": "",}
#     )
#     if request.method == "POST":
#         formset = ReviewFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             formset.save()
#             # do something
#     else:
#         formset = ReviewFormSet()
#     return render(request, "reviews/manage.html", {"formset": formset})


##########################################################################
""" Cycle Views """
##########################################################################

# class BaseCycleFormSet(BaseModelFormSet):
#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.queryset = ReviewCycle.objects.filter(review=parent)

# def manage_permit_review_cycles(request, parent):
#     CycleFormSet = modelformset_factory(
#         ReviewCycle,
#         fields=["__all__"],
#         # exclude=["__all__"],
#         formset=BaseCycleFormSet(review=parent)
#         # widgets = {"": "",}
#     )
#     if request.method == "POST":
#         formset = CycleFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             formset.save()
#             # do something
#     else:
#         formset = CycleFormSet()
#     return render(request, "reviews/cycles.html", {"formset": formset})

##########################################################################
""" End File """
##########################################################################