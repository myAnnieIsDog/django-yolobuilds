##########################################################################
""" Profile Models """
##########################################################################
""" Profile objects have an optional OneToOne relationship with the 
django default User objects to act as an extension of the User model."""
##########################################################################
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """ 
    Extends User: https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User 
    """
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, null=True, blank=True, 
        related_name="user_profile")
    first = models.CharField("First Name", max_length=100)
    last = models.CharField("Last Name", max_length=100)
    company_name = models.CharField(max_length=40, blank=True)
    
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)

    def __str__(self) -> str:
        return f"{self.last}, {self.first}"
    
    def get_username(self) -> str:
        return self.user.username
    
    def get_full_name(self):
        return f"{self.first} {self.last}"
    

##########################################################################
""" PROFESSIONALS """
##########################################################################


class LicenseAgency(models.Model):
    agency_short = models.CharField(max_length=7, unique=True)
    agency_long = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.agency_long
    
    class Meta:
        verbose_name = "License Agency"
        verbose_name_plural = "License Agencies"

class LicenseType(models.Model):
    licensing_agency = models.ForeignKey(LicenseAgency, on_delete=models.PROTECT, null=True)
    license_short = models.CharField(max_length=7, unique=True)
    license_long = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.license_long

    class Meta:
        ordering = ["license_short"]
        verbose_name = "License Type"
        verbose_name_plural = "License Types"

class LicenseHolder(models.Model):
    license_holder = models.ForeignKey(Profile, on_delete=models.PROTECT)
    license_type = models.ForeignKey(LicenseType, on_delete=models.PROTECT)
    license_number = models.CharField(max_length=255, unique=True)
    expiration_date = models.DateField()
    verified_valid = models.BooleanField()
    # replace the following with a relationship to business license records.
    bl_number = models.CharField(
        "Yolo County Business License Number", max_length=40, blank=True)

    def __str__(self) -> str:
        return f"{self.license_holder} {self.license_type}"
    
    class Meta:
        ordering = ["license_holder", "license_type"]


##########################################################################
""" STAFF AND PARTNERS """
##########################################################################


class AgencyOptions(models.Model):
    agency_option_short = models.CharField(max_length=25, unique=True)
    agency_option_full = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.agency_option_short
    
    class Meta:
        ordering = ["agency_option_short"]
        verbose_name = "Partner Agency"
        verbose_name_plural = "Partner Agency Options"

class DepartmentOptions(models.Model):
    department_option_short = models.CharField(max_length=25, unique=True)
    department_option_full = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.department_option_short
    
    class Meta:
        ordering = ["department_option_short"]
        verbose_name = "Department"
        verbose_name_plural = "Department Options"

class DivisionOptions(models.Model):
    division_options = models.CharField(max_length=25, unique=True)

    def __str__(self) -> str:
        return self.division_options
    
    class Meta:
        ordering = ["division_options"]
        verbose_name = "Division"
        verbose_name_plural = "Division Options"

class Staff(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.PROTECT, related_name="staff_profile")
    department = models.ForeignKey(
        DepartmentOptions, on_delete=models.PROTECT)
    division = models.ForeignKey(
        DivisionOptions, on_delete=models.PROTECT)
    supervisor = models.CharField(max_length=255, null=True, blank=True)
    supervisor_email = models.CharField(max_length=255, null=True, blank=True)
    # recent_records = models.ManyToManyField(Record)

    def __str__(self) -> str:
        return self.profile.user.username
    
    class Meta():
        verbose_name_plural = "Staff Member"
        verbose_name_plural = "Staff Members"

class YoloCountyPartners(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.PROTECT)
    agency = models.ForeignKey(
        AgencyOptions, on_delete=models.PROTECT)
    alt_contact_name = models.CharField(max_length=255, null=True, blank=True)
    alt_contact_email = models.CharField(max_length=255, null=True, blank=True)
    # recent_records = models.ManyToManyField(Record)

    def __str__(self) -> str:
        return self.profile.user.username
    
    class Meta():
        verbose_name_plural = "Staff for Partner Agency"
        verbose_name_plural = "Staff for Partner Agencies"


##########################################################################
""" End File """
##########################################################################