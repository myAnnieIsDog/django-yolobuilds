from django.shortcuts import render
from django.forms import modelformset_factory, BaseModelFormSet
from .models import ReviewType, ReviewStatus, Review, ReviewCycle


##########################################################################
""" Review Views """
##########################################################################

class BaseReviewFormSet(BaseModelFormSet):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Review.objects.filter(permit=parent)

def manage_permit_reviews(request, parent):
    ReviewFormSet = modelformset_factory(
        Review,
        fields=["__all__"],
        # exclude=["__all__"],
        formset=BaseReviewFormSet(permit=parent)
        # widgets = {"": "",}
    )
    if request.method == "POST":
        formset = ReviewFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something
    else:
        formset = ReviewFormSet()
    return render(request, "reviews/manage.html", {"formset": formset})


##########################################################################
""" Cycle Views """
##########################################################################

class BaseCycleFormSet(BaseModelFormSet):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = ReviewCycle.objects.filter(review=parent)

def manage_permit_review_cycles(request, parent):
    CycleFormSet = modelformset_factory(
        ReviewCycle,
        fields=["__all__"],
        # exclude=["__all__"],
        formset=BaseCycleFormSet(review=parent)
        # widgets = {"": "",}
    )
    if request.method == "POST":
        formset = CycleFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something
    else:
        formset = CycleFormSet()
    return render(request, "reviews/cycles.html", {"formset": formset})

##########################################################################
""" End File """
##########################################################################