##########################################################################
""" Building Permit Base Model """
##########################################################################
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from records.models import Record
from profiles.models import Profile
from inspections.models import InspectionType
from reviews.models import ReviewType




class BP(models.Model):
    record = models.OneToOneField(Record, on_delete=models.PROTECT)
    suffix = models.CharField(max_length=4, default="0000")
    valuation = models.DecimalField(
        max_digits=15, decimal_places=2, default=2000)
    
    owner_builder_form = models.BooleanField(
        "Owner-Builder Form Acknowledgement", default=False)
    owner_rep_form = models.BooleanField(
        "Owner's Authorization of a Representative", default=False)
    CSLB_Forms = models.BooleanField(
        "CSLB License Verification", default=False)
    employee_authorization = models.BooleanField(
        "CSLB Licensed Employer Authorization of Employee to Pull Permits", default=False)
    
    finaled = models.DateTimeField(null="True")
    finaled_by = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="finaler")
    expiration_date = models.DateTimeField(null=True,
        help_text="""
        Building Permits expire 12 months after 
        they are issued, except that they are 
        extended for specific reasons in 
        accordance with County policy.
        """)
    expiration_set_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True, 
        related_name="expirer")
    issued = models.DateTimeField(null=True)
    issued_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True, 
        related_name="issuer")
    approved = models.DateTimeField(null=True)
    approved_by = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="approver")
    received = models.DateTimeField(null=True)
    received_by = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="receiver")

    def __str__(self) -> str:
        return self.building_permit.__str__()
    
    def apply():
        # run_application_checks()
        # add_inspections()
        # add_reviews()
        # add_fees()
        pass

    def pay_application_fees():
        pass

    def receive(self, request):
        # run_application_checks()
        # prepare_documents()
        self.received = timezone.now()
        self.received_by = request.user.id
        # send_application_receipt_email()

    def approve(self, request):
        # run_issuance_checks()
        # prepare_approval_documents()
        # prepare_issuance_documents()
        self.status = "Issued"
        self.approved = timezone.now()
        self.approved_by = request.user.id
        self.save()
        # send_approval_email()

    def pay_issuance_fees():
        pass

    def issue(self, request):
        self.issued = timezone.now()
        self.issued_by = request.user.id
        self.expiration_date = timezone.now() + timezone.timedelta(days=365)
        self.expiration_set_by = request.user.id
        self.save()

    def extend_expiration(self, request, extra_days=180):
        a = self.expiration_date + timezone.timedelta(extra_days)
        b = self.issued + timezone.timedelta(days=1095)
        self.expiration_date = min(a, b)
        self.expiration_set_by = request.user.id
        self.save()
    
    def expire(self):
        self.status = "Expired"
        self.save()

    def suspend(self):
        self.status = "Suspended"
        # add_suspended_tag()
        self.save()

    def final(self, request):
        # run_final_checks()
        # prepare_occupancy_documents()
        self.status = "Finaled"
        self.finaled = timezone.now()
        self.finaled_by = request.user.id
        self.save()
        # send_occupancy_email()

    class Meta:
        verbose_name = "Building Permits"
        verbose_name_plural = "Building Permits"


##########################################################################
""" Building """
##########################################################################

class Building(models.Model):
    bldg_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    accessory_utility_new_area = models.PositiveIntegerField(default=0)
    residential_dwelling_new_units = models.PositiveIntegerField(default=0)
    residential_dwelling_new_area = models.PositiveIntegerField(default=0)
    assembly_new_area = models.PositiveIntegerField(default=0)
    office_new_area = models.PositiveIntegerField(default=0)
    processing_or_production_new_area = models.PositiveIntegerField(default=0)
    warehouse_new_area = models.PositiveIntegerField(default=0)
    retail_new_area = models.PositiveIntegerField(default=0)
    other_new_area = models.PositiveIntegerField(default=0)
    other_description = models.PositiveIntegerField(default=0)

    review_days = 10
    # reviews = models.ManyToManyField(ReviewType, related_name="revs")
    default_reviews = [
        "Building (Full)", 
        "Env. Health", 
        "Fire District", 
        "Int. Waste Management", 
        "Planning", 
        "Public Works"]
    # inspections = models.ManyToManyField(InspectionType, related_name="insps")
    fees = [""]
    notes = ""

    class Meta:
        verbose_name = "New Building/Structure"
        verbose_name_plural = "New Buildings/Structures"


##########################################################################
""" Demolition """
##########################################################################

class Demolition(models.Model):
    demolition_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    number_of_structures = models.PositiveSmallIntegerField(default=1)
    building_area = models.PositiveIntegerField(default=1000)
    review_days = 10
    notes = []

    class Meta:
        ordering = ["demolition_permit"]
        verbose_name = "Demolition Permits"
        verbose_name_plural = "Demolition Permits"

    def default_reviews(sender, **kwargs):  # django.db.models.signals.post_save
        return ["Bldg Demolition"] 
    reviews = models.ManyToManyField(ReviewType,default=default_reviews)
    
    def default_inspections(sender, **kwargs):  
        # django.db.models.signals.post_save
        return [
            "Demolition 1 Pre-Measure and Utility Disconnect", 
            "Demolition 2 Final"
        ]
    inspections = models.ManyToManyField(InspectionType,blank=True)

##########################################################################
""" Electrical """
##########################################################################
class Electrical(models.Model):
    elc_record = models.OneToOneField(BP, on_delete=models.PROTECT)

    service_changeout = models.BooleanField(default=False)
    service_phases = models.PositiveIntegerField(default=1)
    service_voltage = models.CharField(max_length=255, default="120/240 V")
    service_current = models.PositiveIntegerField(default=150, help_text="A")
    serving = models.CharField(max_length=255, default='A Single Residential Dwelling Unit')

    general_lighting_and_receptacles = models.PositiveIntegerField(blank=True, help_text="square feet of the area served")
    pv_solar_roof = models.PositiveIntegerField(blank=True, help_text="kW ac")
    solarAPP = models.BooleanField(default=False)
    pv_solar_ground = models.PositiveIntegerField(blank=True, help_text="kW ac")  
    ess_current = models.PositiveIntegerField(blank=True, help_text="24 A")
    ess_capacity = models.PositiveIntegerField(blank=True, help_text="14 kWh")
    evcs = models.PositiveIntegerField(blank=True, help_text="24 A")
    generator_power = models.PositiveIntegerField(blank=True, help_text="14 kWh")
    generator_fuel = models.CharField(max_length=255, default="Propane")
    motor_loads = models.PositiveIntegerField(blank=True)

    review_days = models.PositiveIntegerField(default=10)
    reviews = ["Bldg Electrical"]
    inspections = ["** PERMIT FINAL **"]
    notes = []

    def __str__(self) -> str:
        return self.elc_record.bldg_permit.number

    def add_reviews():
        pass
    
    def add_fees():
        pass
    
    def add_insp():
        pass

    def add_notes(self):   
        if self.solarAPP:
            self.notes.append("Plans approved by SolarAPP+ can start work immediately, even if there is an error processing this permit application. At inspection provide the SolarAPP+ checklist.")

        if self.ess_current or self.ess_capacity:
            self.notes.append("At inspection provide the Energy Storage System (Battery) manufacturer's installation instructions.")
        
        if self.generator_power or self.generator_fuel:
            self.notes.append("At inspection provide the Generator manufacturer's installation instructions.")
        
        if self.evcs:
            self.notes.append("At inspection provide the EVCS manufacturer's installation instructions.")

        if self.pv_solar_ground:
            self.notes.append("At inspection provide the manufacturer's installation instructions for all Solar Equipment, including panels, dc-dc converters (optimizers), micro- or central-inverters, rapid shut-down, disconnects, racking, foundation systems, etc.")

        elif self.pv_solar_roof:
            self.notes.append("At inspection provide the manufacturer's installation instructions for all Solar Equipment, including panels, dc-dc converters (optimizers), micro- or central-inverters, rapid shut-down, disconnects, racking, etc.")

    class Meta:
        ordering = ["elc_record"]
        verbose_name = "Electrical Permit"
        verbose_name_plural = "Electrical Permits"


##########################################################################
""" Existing Building/Structure """
##########################################################################
class Reroof(models.Model):
    bp = models.OneToOneField(Building, on_delete=models.PROTECT)
    suffix = "OTC-Bld"
    reroof_area = models.PositiveIntegerField(default=0)
    fire_class = models.CharField(max_length=1)
    cf1r = models.BooleanField(default=False)
    reviews = ["CF1R"]
    inspections = ["Roof Deck Nail", "Final"]

class Stucco(models.Model):
    suffix = "OTC-Bld"
    type = models.CharField(max_length=255, default="Stucco")
    area = models.PositiveIntegerField(default=0)
    fire_class = models.CharField(max_length=1)
    class Meta():
        verbose_name = "Replace Exterior Wall (Siding/Stucco)"

class Windows(models.Model):
    suffix = "OTC-Win"
    number_of_window = models.PositiveIntegerField(default=0)
    new_area = models.PositiveIntegerField(default=0)
    replacement_area = models.PositiveIntegerField(default=0)
    cf1r = models.BooleanField(default=False)
    hazardous_locations = models.BooleanField(default=False)
    notes = "At inspection provide the CF2R and the installation instructions."
    class Meta():
        verbose_name = "Window Replacement"


##########################################################################
""" Fire """
##########################################################################


class Fire(models.Model):
    fire_protection_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    suffix = "Fire"
    sprinkler_heads = models.PositiveIntegerField(default=20)
    sprinkler_area = models.PositiveIntegerField(default=2000)

    new_alarm_system = models.BooleanField(False)
    fire_detectors = models.PositiveIntegerField(default=20)

    hazardous_material = models.BooleanField(False)
    high_piled_combustible_storage = models.BooleanField(False)

    class Meta:
        verbose_name = "Fire Protection Permits"
        verbose_name_plural = "Fire Protection Permits"

##########################################################################
""" Flood """
##########################################################################


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

class Flood(models.Model):
    flood_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    zone = models.ForeignKey(FloodZones, on_delete=models.PROTECT)
    bfe = models.PositiveIntegerField(null=True)
    design_depth = models.PositiveIntegerField(null=True)

    FEMA_defined_structure = models.BooleanField(null=True)
    substantial_improvement = models.BooleanField(null=True)
    variance = models.BooleanField(null=True)

    review_days = 20
    reviews = ["FZ Materials", "FZ Anchoring", "FZ Drainage", "FZ Elevation", "FZ Utilities", "FZ Venting"]
    inspections = ["Lowest Floor", "Final"]
    notes = []

    def __str__(self) -> str:
        return f"{self.flood_permit}-Fld"

    class Meta:
        verbose_name = "Flood Protection Permits"
        verbose_name_plural = "Flood Protection Permits"

##########################################################################
""" Grading """
##########################################################################

class Grading(models.Model):
    grading_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    purpose = models.CharField(max_length=20, null=True)
    disturbed_area = models.PositiveIntegerField(default=1000)
    max_cut_depth = models.PositiveIntegerField(default=3)
    max_cut_slope = models.PositiveIntegerField(default=3)
    max_fill_height = models.PositiveIntegerField(default=3)
    max_fill_slope = models.PositiveIntegerField(default=3)
    geotech_report = models.BooleanField(default=True)
    special_inspection = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.grading_permit}-Grd"
    
    class Meta:
        ordering = ["grading_permit"]
        verbose_name = "Grading Permits"
        verbose_name_plural = "Grading Permits"

##########################################################################
""" Mechanical """
##########################################################################

class Mechanical(models.Model):
    mechanical_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    equipment_units = models.PositiveIntegerField(default=1)
    hvac_units = models.PositiveIntegerField(default=1)
    hvac_type = models.CharField(max_length=255, default="Split")
    hvac_capacity = models.PositiveIntegerField(default=2)
    length_of_ductwork = models.PositiveIntegerField(default=0)
    process_piping = models.PositiveIntegerField(default=1)


    def __str__(self) -> str:
        return f"{self.mechanical_permit}-Mch"
    
    def add_notes(self):
        if self.wh_type or self.wh_capacity:
            self.notes.append("At inspection provide the CF2R, CF3R and the manufacturer's installation instructions.")

    class Meta:
        ordering = ["mechanical_permit"]
        verbose_name = "Mechanical Permits"
        verbose_name_plural = "Mechanical Permits"


##########################################################################
""" Plumbing """
##########################################################################
class Plumbing(models.Model):
    plumbing_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    general_fixtures = models.PositiveIntegerField(default=1000)

    water_supply_service = models.PositiveIntegerField(default=100)
    waste_water_service = models.PositiveIntegerField(default=100)

    sewer_diameter = models.PositiveIntegerField(blank=True)
    sewer_material = models.CharField(max_length=55, help_text="ABS")
    sewer_trenchless = models.BooleanField(default=False)

    wh_type = models.CharField(max_length=255, default="Heat Pump")
    wh_capacity = models.PositiveIntegerField(default=50)

    fuel = models.CharField(max_length=55, help_text="Propane")
    fuel_gas_appliance = models.PositiveIntegerField(default=1000)
    fuel_gas_pipe_length = models.PositiveIntegerField(blank=True)
    fuel_gas_pipe_diameter = models.PositiveIntegerField(blank=True)
    fuel_gas_pipe_material = models.CharField(max_length=55, help_text="Metal")
    
    propane_capacity = models.PositiveIntegerField(blank=True)
    propane_underground = models.BooleanField(default=False)
    propane_setback_to_structures = models.PositiveIntegerField(blank=True)

    def __str__(self) -> str:
        return f"{self.plumbing_permit}-Plb"

    def add_notes(self):
        if self.wh_type or self.wh_capacity:
            self.notes.append("At inspection provide the CF2R and the installation instructions.")

    class Meta:
        ordering = ["plumbing_permit"]
        verbose_name = "Plumbing Permits"
        verbose_name_plural = "Plumbing Permits"


##########################################################################
""" Pool """
##########################################################################
class Pool(models.Model):
    pool_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    public = models.BooleanField(default=False)
    area = models.PositiveIntegerField("Area (square feet)", blank=True)
    depth = models.PositiveIntegerField("Depth (feet)", blank=True)

    enclosure = models.BooleanField(default=False)
    structural = models.BooleanField(default=False)
    accessibility = models.BooleanField(default=False)

    reviews = models.ManyToManyField(ReviewType, blank=True)
    inspections = models.ManyToManyField(InspectionType, blank=True)
    notes = []

    def __str__(self) -> str:
        return f"{self.pool_permit}-Pool"
    
    class Meta:
        ordering = ["pool_permit"]
        verbose_name = "Pool/Spa Permits"
        verbose_name_plural = "Pool/Spa Permits"


##########################################################################
""" All Models """
##########################################################################
all_models = (
    BP,
    Building,
    Demolition,
    Electrical,
    Fire,
    FloodZones,
    Flood,
    Grading,
    Mechanical,
    Plumbing,
    Pool
)
##########################################################################
""" End File """
##########################################################################