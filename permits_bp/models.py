from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from records.models import Record, Type
from locations.models import FloodZones

##########################################################################
""" Building Permit Base Model """
##########################################################################

class UseGroup(models.Model):
    group = models.CharField(max_length=7)
    description = models.CharField(max_length=55)


class TypeOfConstruction(models.Model):
    type = models.CharField(max_length=7)
    description = models.CharField(max_length=55)


class BP(models.Model):
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
    
    finaled = models.DateTimeField(null="True", blank=True)
    finaled_by = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="finaler")
    expiration_date = models.DateTimeField(null=True, blank=True,
        help_text="""
        Building Permits expire 12 months after 
        they are issued, except that they are 
        extended for specific reasons in 
        accordance with County policy.
        """)
    expiration_set_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True, 
        related_name="expirer")
    issued = models.DateTimeField(null=True, blank=True)
    issued_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True, 
        related_name="issuer")
    approved = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="approver")
    received = models.DateTimeField(null=True, blank=True)
    received_by = models.ForeignKey(
        User, on_delete=models.PROTECT, 
        null=True, blank=True, 
        related_name="receiver")
   
    def apply():
        # run_application_checks()
        # add_inspections()
        # add_reviews()
        # add_fees()
        pass

    def pay_application_fees():
        pass

    def receive(self, request):
        self.number = self.set_number()
        self.division = "Building"
        self.status = "Under Review"
        self.forms.add(id = [1, 2, 3, 4]) # Air District, EH, IWM, Fire District
        self.reviews.add(id = 9) # Bldg Demolition
        self.inspections.add(id = [17, 18, 31]) # Demo 1, Demo 2, Permit Final
        self.fees.add(id = [601, 603, 608, 610, 613, 614, 644, 645, 810])
        self.received = timezone.now()
        self.received_by = request.user.id
        self.expiration_date = self.received + timezone.timedelta(days = 365)
        # run_application_checks()
        # prepare_documents()
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

    def reinstate(self):
        if self.was_issued:
            self.status = "Issued"
        else:
            self.status = "Under Review"

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

    def __str__(self) -> str:
        return self.number
    
    class Meta:
        ordering = ["number"]
        verbose_name = "BP"
        verbose_name_plural = "BP's"


class Building(models.Model):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

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

    def __str__(self) -> str:
        return f"{self.number}-New"
    
    class Meta:
        verbose_name = "New Building/Structure"
        verbose_name_plural = "New Buildings/Structures"


class Demolition(models.Model):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    suffix = "-Demo"
    type_of_structure = models.CharField(max_length = 55, null=True, blank = True)
    demolition_area = models.CharField(max_length = 55)
    options = {
        "accessory": "Accessory", 
        "commercial": "Commercial", 
        "residential": "Residential", 
        "partial": "Partial", 
        "pool": "Pool",
    }

    def __str__(self) -> str:
        return f"{self.number}-Demo"
    
    def add_reviews(self):
        self.reviews.add(review_type__startswith="Bldg Demo")

    def add_inspections(self):
        self.inspections.add(inspection_type__startswith="Demo")
    
    def add_fees(self):
        self.fees.add(fee_name="Demolition")
        self.fees.add(fee_name="Demolition of Swimming Pool")
    
    class Meta:
        ordering = ["number"]
        verbose_name = "Demolition Permits"
        verbose_name_plural = "Demolition Permits"


class Electrical(models.Model):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    service_changeout = models.BooleanField(default=False)
    service_phases = models.PositiveIntegerField(default=1)
    service_voltage = models.CharField(max_length=255, default="120/240 V")
    service_current = models.PositiveIntegerField(default=150, help_text="A")
    serving = models.CharField(max_length=255, default='A Single Residential Dwelling Unit')

    general_lighting_and_receptacles = models.PositiveIntegerField(blank=True, help_text="Square feet of the area served")
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
        return f"{self.number}-Elc"

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
        ordering = ["number"]
        verbose_name = "Electrical Permit"
        verbose_name_plural = "Electrical Permits"


class Existing(models.Model):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    existing_use = models.ForeignKey(UseGroup, on_delete=models.PROTECT)
    existing_type_of_construction = models.ForeignKey(TypeOfConstruction, on_delete=models.PROTECT)
    existing_building_area = models.PositiveSmallIntegerField("Existing Building Area (square feet)", default=0)

    addition_area = models.PositiveSmallIntegerField(default=0)
    addition_use = models.CharField(max_length=255, default="R-3 Residential Dwelling")

    alteration_area = models.PositiveSmallIntegerField(default=0)
    alteration_use = models.CharField(max_length=255, default="R-3 Residential Dwelling")

    reroof_area = models.PositiveIntegerField(default=0)
    reroof_fire_class = models.CharField(max_length=1)
    reroof_cool_roof = models.BooleanField(default=False)

    ext_wall_replacement_type = models.CharField(max_length=255, default="Stucco")
    ext_wall_replacement_area = models.PositiveSmallIntegerField(default=0)
    ext_wall_replacement_fire_class = models.CharField(max_length=1)

    window_replacement_quantity = models.PositiveSmallIntegerField(default=0)
    window_replacement_like_for_like_area = models.PositiveSmallIntegerField(default=0)
    window_replacement_new_area = models.PositiveSmallIntegerField(default=0)
    window_replacement_cf1r = models.BooleanField(default=False)
    window_replacement_hazardous_locations = models.BooleanField(default=False)

    # def __str__(self) -> str:
    #     return f"{self.number}-Ex"
    
    class Meta:
        # ordering = ["number"]
        verbose_name = "Existing Building Code Permit"
        verbose_name_plural = "Existing Building Code Permits"


class Fire(models.Model):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    suffix = "Fire"
    sprinkler_heads = models.PositiveIntegerField(default=20)
    sprinkler_area = models.PositiveIntegerField(default=2000)

    new_alarm_system = models.BooleanField(False)
    fire_detectors = models.PositiveIntegerField(default=20)

    hazardous_material = models.BooleanField(False)
    high_piled_combustible_storage = models.BooleanField(False)

    def __str__(self) -> str:
        return f"{self.number}-Fire"
    
    class Meta:
        ordering = ["number"]
        verbose_name = "Fire Protection Permits"
        verbose_name_plural = "Fire Protection Permits"


class Flood(models.Model):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    zone = models.ForeignKey(FloodZones, on_delete=models.PROTECT)
    bfe = models.PositiveIntegerField(null=True)
    design_depth = models.PositiveIntegerField(null=True)

    FEMA_defined_structure = models.BooleanField(null=True)
    substantial_improvement = models.BooleanField(null=True)
    variance = models.BooleanField(null=True)

    def __str__(self) -> str:
        return f"{self.number}-Fld"

    class Meta:
        # ordering = ["number"]
        verbose_name = "Flood Protection Permits"
        verbose_name_plural = "Flood Protection Permits"


class Grading(models.Model):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    purpose = models.CharField(max_length=20, null=True)
    disturbed_area = models.PositiveIntegerField(default=1000)
    max_cut_depth = models.PositiveIntegerField(default=3)
    max_cut_slope = models.PositiveIntegerField(default=3)
    max_fill_height = models.PositiveIntegerField(default=3)
    max_fill_slope = models.PositiveIntegerField(default=3)
    geotech_report = models.BooleanField(default=True)
    special_inspection = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.number}-Grd"
    
    class Meta:
        ordering = ["number"]
        verbose_name = "Grading Permits"
        verbose_name_plural = "Grading Permits"


class Mechanical(models.Model):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    equipment_units = models.PositiveIntegerField(default=1)
    hvac_units = models.PositiveIntegerField(default=1)
    hvac_type = models.CharField(max_length=255, default="Split")
    hvac_capacity = models.PositiveIntegerField(default=2)
    length_of_ductwork = models.PositiveIntegerField(default=0)
    process_piping = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.number}-Mch"
    
    def add_notes(self):
        if self.wh_type or self.wh_capacity:
            self.notes.append("At inspection provide the CF2R, CF3R and the manufacturer's installation instructions.")

    class Meta:
        ordering = ["number"]
        verbose_name = "Mechanical Permits"
        verbose_name_plural = "Mechanical Permits"


class Plumbing(models.Model):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

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
        return f"{self.number}-Plb"

    def add_notes(self):
        if self.wh_type or self.wh_capacity:
            self.notes.append("At inspection provide the CF2R and the installation instructions.")

    class Meta:
        ordering = ["number"]
        verbose_name = "Plumbing Permits"
        verbose_name_plural = "Plumbing Permits"


class Pool(models.Model):
    record_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)

    public = models.BooleanField(default=False)
    area = models.PositiveIntegerField("Area (square feet)", blank=True)
    depth = models.PositiveIntegerField("Depth (feet)", blank=True)

    enclosure = models.BooleanField(default=False)
    structural = models.BooleanField(default=False)
    accessibility = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.number}-Pool"
    
    class Meta:
        ordering = ["number"]
        verbose_name = "Pool/Spa Permits"
        verbose_name_plural = "Pool/Spa Permits"

##########################################################################
""" End File """
##########################################################################