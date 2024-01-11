from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

##########################################################################
""" Location Models """
##########################################################################

def apn_string_to_display(input: str) -> str:
    book, page, parcel = input[:-6], input[-6:-3], input[-3:]
    return f"{book}-{page}-{parcel}"

class District(models.Model): 
    dist_type = models.CharField(max_length=100)
    district = models.CharField(max_length=55)
    description = models.CharField(max_length=255, null=True, blank=True)

    address = models.CharField(max_length=255, null=True, blank=True)
    city_state_zip = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.district} {self.dist_type}"


class Jurisdiction(models.Model): 
    jurisdiction = models.CharField(max_length=55)

    def __str__(self) -> str:
        return f"{self.jurisdiction}"



##########################################################################
""" Parcel Model """
##########################################################################

class Parcel(models.Model): 
    book = models.CharField(max_length=3, default="000")
    page = models.CharField(max_length=3, default="000")
    parcel = models.CharField(max_length=3, default="000")
    active = models.BooleanField(default=True)
    owner_name = models.CharField(
        max_length=100, null=True, blank=True)
    owner_address = models.CharField(
        max_length=100, null=True, blank=True)
    land_use_zone = models.CharField(max_length=10, default="A-N")
    wui_sra = models.BooleanField()
    wui_lra = models.BooleanField()
    wui_risk = models.DecimalField(
        max_digits=1, decimal_places=0, default=0)
    wui_regulations = models.BooleanField()
    flood_a = models.BooleanField()
    flood_ae = models.BooleanField()
    flood_ao = models.BooleanField()
    flood_x = models.BooleanField()
    floodway = models.BooleanField()

    jurisdiction = models.ForeignKey(
        Jurisdiction, on_delete=models.PROTECT, null=True, blank=True)
    districts = models.ManyToManyField(District, blank=True)
    
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    
    parcels = models.ManyToManyField("self", blank=True)
    # addresses = one to many; see foreign key below
    # bl = models.ManyToManyField(SiteAddress, blank=True)
    # bp = models.ManyToManyField(BP, blank=True)
    # ce = models.ManyToManyField(SiteAddress, blank=True)
    # pw = models.ManyToManyField(SiteAddress, blank=True)
    # zf = models.ManyToManyField(SiteAddress, blank=True)

    def __str__(self) -> str:
        return f"{self.book}-{self.page}-{self.parcel}"

##########################################################################
""" Address Model """
##########################################################################
class CityStZip(models.Model):
    city = models.CharField(max_length=55, blank=True)
    state = "CA"
    zip = models.CharField(max_length=25, blank=True)

    def __str__(self) -> str:
        return f"{self.city}, {self.state} {self.zip}" 
    
    class Meta:
        verbose_name = "City, State Zip"
        verbose_name_plural = "City, State Zip"

class SiteAddress(models.Model): 
    """ Inherits Label, Description, Created, Modified """
    parcel = models.ForeignKey(
        Parcel, on_delete=models.PROTECT, null=True, blank=True)
    number = models.CharField(max_length=10, default="12345")
    street = models.CharField(max_length=50, default="County Road 98")
    city_st_zip = models.ForeignKey(CityStZip, on_delete=models.PROTECT, null=True, blank=True)
    geolocation = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.number} {self.street}"
    
    class Meta:
        verbose_name = "Site Address"
        verbose_name_plural = "Site Addresses"

##########################################################################
""" All Models """
##########################################################################
all_models = (
    District,
    Jurisdiction,
    Parcel,
    SiteAddress,
)
##########################################################################
""" End File """
##########################################################################