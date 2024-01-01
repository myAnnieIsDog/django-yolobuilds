from crispy_forms.helper import FormHelper
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import base, detail, list, edit, dates
from .models import Profile


##########################################################################
"""                          Profile Views                             """
##########################################################################

common_fields = [
            "first", 
            "last",
            "company_name",
            "email", 
            "phone_number", 
            "address", 
            "city", 
            "state", 
            "zip", 
        ]

class ProfileCreateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, edit.CreateView):
    template_name = "layout_form.html"
    model = Profile
    exclude = [
        "user",
        "display_mode",
        "home_page",
        "recent_records",
        "modified_on",
        "modified_by",
        "create_on",
        "create_by",
    ]
    extra_context = {
        "heading": "Create Profile", 
        "intro": "Use this form to create a user profile. A valid email is required to verify your profile.",
        "button_text": "Submit"}
    success_url = "profile-update"
    success_message = "The profile for %(first_name)s %(last_name)s was created successfully."  

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()


class ProfileDetailView(detail.DetailView):
    template_name = "layout_form.html"
    model = Profile
    fields = "__all__"
    extra_context = {
        "heading": "Update Profile", 
        "intro": "Use this form to update your user profile.", 
        "button_text": "Update"}
    success_url = "profile-update"
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()


class ProfileUpdateView(edit.UpdateView):
    template_name = "layout_form.html"
    model = Profile
    exclude = [
        "modified_on",
        "modified_by",
        "create_on",
        "create_by",
    ]
    extra_context = {
        "heading": "Update Profile", 
        "intro": "Use this form to update your user profile.", 
        "button_text": "Update"}
    success_url = "profile-update"
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()

