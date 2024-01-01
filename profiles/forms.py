from django import forms
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField
from .models import Profile


class ProfileForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Profile #, User
        fields = [
            "user", 
            "company_name", 
            "phone_number", 
            "address", 
            "city", 
            "state", 
            "zip", 
        ]
        # Add a method to also generate a User for the profile when generated online. The method should be optional when staff creates a profile to add to an application.