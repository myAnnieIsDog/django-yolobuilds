from django.db import models

##########################################################################
""" Location Models """
##########################################################################

def apn_string_to_display(input: str) -> str:
    book, page, parcel = input[:-6], input[-6:-3], input[-3:]
    return f"{book}-{page}-{parcel}"

class DistrictType(models.Model): 
    type = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.type

    class Meta():
        ordering = ["type"]
        verbose_name = "District Type"
        verbose_name_plural = "District Types"

class District(models.Model): 
    type = models.ForeignKey(DistrictType, on_delete=models.PROTECT)
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)

    address = models.CharField(max_length=255, null=True, blank=True)
    city_state_zip = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.name} {self.type}"

class Jurisdiction(models.Model): 
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)

    address = models.CharField(max_length=255, null=True, blank=True)
    city_state_zip = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

##########################################################################
""" Parcel Model """
##########################################################################

class Parcel(models.Model): 
    book = models.CharField(max_length=3, default="000")
    page = models.CharField(max_length=3, default="000")
    parcel = models.CharField(max_length=3, default="000")
    
    active = models.BooleanField(default=True)
    parents = models.ManyToManyField("self")
    
    owner_name = models.CharField(
        max_length=100, null=True, blank=True)
    owner_address = models.CharField(
        max_length=100, null=True, blank=True)

    land_use_zone = models.CharField(max_length=10, default="A-N")
    jurisdiction = models.ForeignKey(
        Jurisdiction, on_delete=models.PROTECT, null=True, blank=True)
    districts = models.ManyToManyField(District)

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

    def __str__(self) -> str:
        return f"{self.book}-{self.page}-{self.parcel}"

##########################################################################
""" Address Model """
##########################################################################

class SiteAddress(models.Model): 
    """ Inherits Label, Description, Created, Modified """
    parcel = models.ForeignKey(Parcel, on_delete=models.PROTECT)
    number = models.CharField(max_length=10, default="12345")
    street = models.CharField(max_length=50, default="CR 98")
    city = models.CharField(max_length=50, default="Woodland")
    state = models.CharField(max_length=2, default="CA")
    zip = models.CharField(max_length=5, default="95695")
    geolocation = models.CharField(max_length=50, null=True, blank=True)

##########################################################################
""" End File """
##########################################################################