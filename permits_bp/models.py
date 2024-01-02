##########################################################################
""" Building Permit Base Model """
##########################################################################
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from permits.models import Permit, InspectionType, ReviewType
from profiles.models import Profile

class ApplicantRole(models.Model):
    applicant_role_options = models.CharField(max_length=55, unique=True)
    # applicant_role_options = [
    #         "Property Owner", 
    #         "Property Owner's Authorized Agent", 
    #         "CSLB Licensed Contractor", 
    #         "CSLB Licensed Contractor's Authorized Employee",
    #     ]

class OwnerRole(models.Model):
    owner_role_options = models.CharField(max_length=55, unique=True)
    # owner_role_options = [
    #         "Performing all of the work, except for employess earning $500 or less for the entire project.", 
    #         "Hiring CSLB Licensed Contractors and verifying the contractor's worker's compensation insurance.", 
    #         "Hiring employee's earning $500 or more and paying for worker's compensation insurance.", 
    #     ]

class BP(models.Model):
    building_permit = models.OneToOneField(Permit, on_delete=models.PROTECT)
    suffix = models.CharField(max_length=4, default="0000")
    valuation = models.DecimalField(
        max_digits=15, decimal_places=2, default=2000)
    
    applicant_role = models.ForeignKey(ApplicantRole, on_delete=models.PROTECT)
    contractor = models.ForeignKey(Profile, on_delete=models.PROTECT, 
        null=True, blank=True, related_name="contrs") 
    designer = models.ForeignKey(Profile, on_delete=models.PROTECT, 
        null=True, blank=True, related_name="designs")

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


##########################################################################
""" Building """
##########################################################################


class Building(models.Model):
    building_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    suffix = "Bldg"
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

    review_days = 20
    reviews = models.ManyToManyField(InspectionType, related_name="revs")
    default_reviews = [
        "Building (Full)", 
        "Env. Health", 
        "Fire District", 
        "Int. Waste Management", 
        "Planning", 
        "Public Works"]
    inspections = models.ManyToManyField(InspectionType, related_name="insps")
    fees = [""]
    notes = ""

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
""" Demolition """
##########################################################################


class Demolition(models.Model):
    demolition_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    suffix = "Demo"
    number_of_structures = models.PositiveSmallIntegerField(default=1)
    building_area = models.PositiveIntegerField(default=1000)
    review_days = 20
    reviews = ["Building (Full)", "Env. Health", "Fire District", "Int. Waste Management", "Planning", "Public Works"]
    inspections = ["Pre-Measure", "Final"]
    notes = ""


##########################################################################
""" Electrical """
##########################################################################


class Electrical(models.Model):
    electrical_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    suffix = "Elc"
    phases = models.PositiveIntegerField(default=1)
    voltage = models.PositiveIntegerField(default=240)
    current = models.PositiveIntegerField(default=100)

    service_drop = models.BooleanField(default=False)
    general_lighting_and_receptacles = models.PositiveIntegerField(default=1000)
    pv_solar_roof = models.PositiveIntegerField(default=10)
    pv_solar_ground = models.PositiveIntegerField(default=100)  
    evcs = models.PositiveIntegerField(default=100)
    backup_generator = models.PositiveIntegerField(default=100)
    ess_battery = models.PositiveIntegerField(default=100)
    motor_loads = models.PositiveIntegerField(default=100)

    review_days = 20
    reviews = ["Building (Full)", "Env. Health", "Fire District", "Int. Waste Management", "Planning", "Public Works"]
    inspections = ["Rough Electrical", "Final"]
    notes = "This permit type is only for work that is not eligible to be expedited."

class ElectricalService(models.Model):
    suffix = "OTC-Elc"
    voltage = models.CharField(max_length=255, default="120/240 V")
    current = models.PositiveIntegerField(default=150)
    phases = models.PositiveIntegerField(default=1)
    reviews = ["Site Map"]
    inspections = ["Meter Release", "Final"]
    notes = "The two inspections can be combined in a single inspection stop."
    class Meta():
        verbose_name = "Electrical Service Replacement/Upgrade"
        
class ESS(models.Model):
    suffix = "OTC-Elc"
    voltage = models.CharField(max_length=255, default="120/240 V")
    current = models.PositiveIntegerField(default=24, help_text="A")
    capacity = models.PositiveIntegerField(default=14, help_text="kWh")
    reviews = ["Site Map", "Electrical Plan"]
    notes = "At inspection provide the installation instructions."
    class Meta():
        verbose_name = "Energy Storage System (Battery)"

class EVCS(models.Model):
    suffix = "OTC-Elc"
    voltage = models.CharField(max_length=255, default="120/240 V")
    current = models.PositiveIntegerField(default=150)
    phases = models.PositiveIntegerField(default=1)
    reviews = ["Site Map", "Electrical Plan"]
    notes = "At inspection provide the installation instructions."
    class Meta():
        verbose_name = "Electrical Vehicle Charging Station"

class Generator(models.Model):
    suffix = "OTC-Elc"
    voltage = models.CharField(max_length=255, default="120/240 V")
    current = models.PositiveIntegerField(default=24)
    phases = models.PositiveIntegerField(default=1)
    fuel = models.CharField(max_length=255, default="Propane")
    reviews = ["Site Map", "Electrical Plan"]
    notes = "At inspection provide the installation instructions."
    class Meta():
        verbose_name = "Backup Generator"

class Solar(models.Model):
    suffix = "OTC-Elc"
    roof_mount = models.BooleanField(default=False)
    capacity = models.DecimalField(max_digits=10, decimal_places=1)
    serving = models.CharField(max_length=255, default='A Single Residential Dwelling')
    solarAPP = models.BooleanField(default=False)
    review_days = 0
    notes = "Plans approved by SolarAPP+ can start work immediately, even if there is an error processing this permit application. At inspection provide the SolarAPP+ checklist."

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


##########################################################################
""" Flood """
##########################################################################


class FloodZones(models.Model):
    zone_code = models.CharField(max_length=7)
    zone_description = models.CharField(max_length=255)
    # FLOOD_ZONE_A = "A", "Approximate A Zone"
    # FLOOD_ZONE_AE = "AE", "Detailed AE Zone"
    # FLOOD_ZONE_AO = "AO", "Shallow Flooding"
    # FLOOD_ZONE_A_FLOODWAY = "A/F", "No-Rise Floodway"
    # FLOOD_ZONE_X = "X", "Not Regulated"
class Flood(models.Model):
    flood_protection_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    suffix = "Flood"
    zone = models.ForeignKey(FloodZones, on_delete=models.PROTECT)
    bfe = models.PositiveIntegerField(null=True)
    design_depth = models.PositiveIntegerField(null=True)

    FEMA_defined_structure = models.BooleanField(null=True)
    substantial_improvement = models.BooleanField(null=True)
    variance = models.BooleanField(null=True)

    review_days = 20
    reviews = ["FZ Materials", "FZ Anchoring", "FZ Drainage", "FZ Elevation", "FZ Utilities", "FZ Venting"]
    inspections = ["Lowest Floor", "Final"]
    notes = "This permit type is only for work that is not eligible to be expedited."


##########################################################################
""" Grading """
##########################################################################


class Grading(models.Model):
    grading_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    suffix = "Grade"
    purpose = models.CharField(max_length=20, null=True)
    disturbed_area = models.PositiveIntegerField(default=1000)
    max_cut_depth = models.PositiveIntegerField(default=3)
    max_cut_slope = models.PositiveIntegerField(default=3)
    max_fill_height = models.PositiveIntegerField(default=3)
    max_fill_slope = models.PositiveIntegerField(default=3)
    geotech_report = models.BooleanField(default=True)
    special_inspection = models.BooleanField(default=True)


##########################################################################
""" Mechanical """
##########################################################################


class Mechanical(models.Model):
    mechanical_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    suffix = "Mch"
    equipment_units = models.PositiveIntegerField(default=1)
    hvac_units = models.PositiveIntegerField(default=1)
    process_piping = models.PositiveIntegerField(default=1)

class HVAC(models.Model):
    suffix = "OTC-Mch"
    type = models.CharField(max_length=255, default="Split")
    capacity = models.PositiveIntegerField(default=2)
    lenght_of_ductwork = models.PositiveIntegerField(default=0)
    reviews = ["CF1R"]
    notes = "At inspection provide the CF2R, CF3R and the installation instructions."
    class Meta():
        verbose_name = "HVAC Replacement"


##########################################################################
""" Plumbing """
##########################################################################


class Plumbing(models.Model):
    plumbing_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    suffix = "Plb"
    water_supply_service = models.PositiveIntegerField(default=100)
    waste_water_service = models.PositiveIntegerField(default=100)
    general_fixtures = models.PositiveIntegerField(default=1000)
    fuel_gas_appliance = models.PositiveIntegerField(default=1000)
    fuel_gas_pipe = models.PositiveIntegerField(default=1000)
    water_heating_heat_pump = models.PositiveIntegerField(default=100)
    water_heating_solar = models.PositiveIntegerField(default=10)
    water_heating_tankless = models.PositiveIntegerField(default=100)

class Propane(models.Model):
    suffix = "OTC-Gas"
    type = models.CharField(max_length=255, default="Tank on Slab/Grade")
    capacity = models.PositiveIntegerField(default=500)
    lenght_of_piping = models.PositiveIntegerField(default=0)
    setback_to_structures = models.PositiveIntegerField(default=10)
    reviews = ["Site Plan", "Fuel Gas Plan"]
    notes = "The two plans can be combined on one sheet."
    class Meta():
        verbose_name = "Install Propane Tank"

class Sewer(models.Model):
    suffix = "OTC-Plb"
    pipe_diameter = models.CharField(max_length=255, default='3"')
    type = models.CharField(max_length=255, default='Trench')
    review = ["Site Plan", "Plumbing Plan"]
    notes = "The two plans can be combined on one sheet."
    class Meta():
        verbose_name = "Building Sewer Replacement"

class WaterHeater(models.Model):
    suffix = "OTC-WH"
    type = models.CharField(max_length=255, default="Heat Pump")
    capacity = models.PositiveIntegerField(default=50)
    notes = "At inspection provide the CF2R and the installation instructions."
    class Meta():
        verbose_name = "Water Heater Replacement"


##########################################################################
""" Pool """
##########################################################################


class Pool(models.Model):
    pool_permit = models.OneToOneField(BP, on_delete=models.PROTECT)
    suffix = "Pool"
    public = models.BooleanField(default=100)
    area = models.PositiveIntegerField(default=1000)
    depth = models.PositiveIntegerField(default=6)

    enclosure = models.BooleanField(default=100)
    structural = models.BooleanField(default=100)
    accessibility = models.BooleanField(default=100)

    review_days = 20
    reviews = ["Building (Accessibility)", "Building (Enclosure)", "Building (Structural)", "Env. Health", "Fire District", "Int. Waste Management", "Planning", "Public Works"]
    inspections = ["Pre-Gunite", "Pre-Deck", "Final/Pre-Plaster/Enclosure"]
    notes = ""

##########################################################################
""" End File """
##########################################################################