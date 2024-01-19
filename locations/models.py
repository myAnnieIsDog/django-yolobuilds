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

    class Meta:
        ordering = ["district"]
        verbose_name = "District"
        verbose_name_plural = "Districts"


class FloodZones(models.Model):
    zone_code = models.CharField("Flood Zone Code", max_length=7)
    zone_description = models.CharField("Flood Zone Description", max_length=255)
    # FLOOD_ZONE_A = "A", "Approximate A Zone"
    # FLOOD_ZONE_AE = "AE", "Detailed AE Zone"
    # FLOOD_ZONE_AO = "AO", "Shallow Flooding"
    # FLOOD_ZONE_A_FLOODWAY = "A/F", "No-Rise Floodway"
    # FLOOD_ZONE_X = "X", "Not Regulated"

    def __str__(self) -> str:
        return self.zone_code
    
    class Meta:
        verbose_name = "Flood Zone"
        verbose_name_plural = "Flood Zones"


class Jurisdiction(models.Model): 
    jurisdiction = models.CharField(max_length=55)

    def __str__(self) -> str:
        return f"{self.jurisdiction}"

    class Meta:
        ordering = ["jurisdiction"]
        verbose_name = "Jurisdiction"
        verbose_name_plural = "Jurisdictions"


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
    parcels = models.ManyToManyField("self", blank=True)
    # addresses = one to many; see foreign key below
    # bl = models.ManyToManyField(SiteAddress, blank=True)
    # bp = models.ManyToManyField(BP, blank=True)
    # ce = models.ManyToManyField(SiteAddress, blank=True)
    # pw = models.ManyToManyField(SiteAddress, blank=True)
    # zf = models.ManyToManyField(SiteAddress, blank=True)

    def __str__(self) -> str:
        return f"{self.book}-{self.page}-{self.parcel}"
    
    class Meta:
        ordering = ["book", "page", "parcel"]
        verbose_name = "Parcel"
        verbose_name_plural = "Parcels"


class CityStZip(models.Model):
    city = models.CharField(max_length=55, blank=True)
    state = "CA"
    zip = models.CharField(max_length=25, blank=True)

    def __str__(self) -> str:
        return f"{self.city}, {self.state} {self.zip}" 
    
    class Meta:
        ordering = ["city", "zip"]
        verbose_name = "City, State Zip"
        verbose_name_plural = "City, State Zip"


class SiteAddress(models.Model): 
    """ Inherits Label, Description, Created, Modified """
    parcel = models.ForeignKey(
        Parcel, on_delete=models.PROTECT, null=True, blank=True)
    number = models.CharField(max_length=10, default="12345")
    street = models.CharField(max_length=50, default="County Road 98")
    city_st_zip = models.ForeignKey(CityStZip, on_delete=models.PROTECT, null=True, blank=True, verbose_name="City, State, Zip")
    geolocation = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.number} {self.street} {self.city_st_zip}"
    
    class Meta:
        ordering = ["number", "street", "city_st_zip"]
        verbose_name = "Site Address"
        verbose_name_plural = "Site Addresses"

##########################################################################
""" End File """
##########################################################################