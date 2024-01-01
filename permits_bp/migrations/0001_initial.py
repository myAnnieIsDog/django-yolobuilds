# Generated by Django 5.0 on 2023-12-31 00:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('permits', '0001_initial'),
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_role_options', models.CharField(max_length=55, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElectricalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voltage', models.CharField(default='120/240 V', max_length=255)),
                ('current', models.PositiveIntegerField(default=150)),
                ('phases', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Electrical Service Replacement/Upgrade',
            },
        ),
        migrations.CreateModel(
            name='ESS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voltage', models.CharField(default='120/240 V', max_length=255)),
                ('current', models.PositiveIntegerField(default=24, help_text='A')),
                ('capacity', models.PositiveIntegerField(default=14, help_text='kWh')),
            ],
            options={
                'verbose_name': 'Energy Storage System (Battery)',
            },
        ),
        migrations.CreateModel(
            name='EVCS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voltage', models.CharField(default='120/240 V', max_length=255)),
                ('current', models.PositiveIntegerField(default=150)),
                ('phases', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Electrical Vehicle Charging Station',
            },
        ),
        migrations.CreateModel(
            name='FloodZones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_code', models.CharField(max_length=7)),
                ('zone_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Generator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voltage', models.CharField(default='120/240 V', max_length=255)),
                ('current', models.PositiveIntegerField(default=24)),
                ('phases', models.PositiveIntegerField(default=1)),
                ('fuel', models.CharField(default='Propane', max_length=255)),
            ],
            options={
                'verbose_name': 'Backup Generator',
            },
        ),
        migrations.CreateModel(
            name='HVAC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Split', max_length=255)),
                ('capacity', models.PositiveIntegerField(default=2)),
                ('lenght_of_ductwork', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'HVAC Replacement',
            },
        ),
        migrations.CreateModel(
            name='OwnerRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_role_options', models.CharField(max_length=55, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Propane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Tank on Slab/Grade', max_length=255)),
                ('capacity', models.PositiveIntegerField(default=500)),
                ('lenght_of_piping', models.PositiveIntegerField(default=0)),
                ('setback_to_structures', models.PositiveIntegerField(default=10)),
            ],
            options={
                'verbose_name': 'Install Propane Tank',
            },
        ),
        migrations.CreateModel(
            name='Sewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pipe_diameter', models.CharField(default='3"', max_length=255)),
                ('type', models.CharField(default='Trench', max_length=255)),
            ],
            options={
                'verbose_name': 'Building Sewer Replacement',
            },
        ),
        migrations.CreateModel(
            name='Solar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roof_mount', models.BooleanField(default=False)),
                ('capacity', models.DecimalField(decimal_places=1, max_digits=10)),
                ('serving', models.CharField(default='A Single Residential Dwelling', max_length=255)),
                ('solarAPP', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stucco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Stucco', max_length=255)),
                ('area', models.PositiveIntegerField(default=0)),
                ('fire_class', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Replace Exterior Wall (Siding/Stucco)',
            },
        ),
        migrations.CreateModel(
            name='WaterHeater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Heat Pump', max_length=255)),
                ('capacity', models.PositiveIntegerField(default=50)),
            ],
            options={
                'verbose_name': 'Water Heater Replacement',
            },
        ),
        migrations.CreateModel(
            name='Windows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_window', models.PositiveIntegerField(default=0)),
                ('new_area', models.PositiveIntegerField(default=0)),
                ('replacement_area', models.PositiveIntegerField(default=0)),
                ('cf1r', models.BooleanField(default=False)),
                ('hazardous_locations', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Window Replacement',
            },
        ),
        migrations.CreateModel(
            name='BP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suffix', models.CharField(default='0000', max_length=4)),
                ('valuation', models.DecimalField(decimal_places=2, default=2000, max_digits=100)),
                ('owner_builder_form', models.BooleanField(default=False, verbose_name='Owner-Builder Form Acknowledgement')),
                ('owner_rep_form', models.BooleanField(default=False, verbose_name="Owner's Authorization of a Representative")),
                ('CSLB_Forms', models.BooleanField(default=False, verbose_name='CSLB License Verification')),
                ('employee_authorization', models.BooleanField(default=False, verbose_name='CSLB Licensed Employer Authorization of Employee to Pull Permits')),
                ('finaled', models.DateTimeField(null='True')),
                ('expiration_date', models.DateTimeField(help_text='\n        Building Permits expire 12 months after \n        they are issued, except that they are \n        extended for specific reasons in \n        accordance with County policy.\n        ', null=True)),
                ('issued', models.DateTimeField(null=True)),
                ('approved', models.DateTimeField(null=True)),
                ('received', models.DateTimeField(null=True)),
                ('applicant_role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.applicantrole')),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='approver', to=settings.AUTH_USER_MODEL)),
                ('building_permit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits.permit')),
                ('contractor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contrs', to='profiles.profile')),
                ('designer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='designs', to='profiles.profile')),
                ('expiration_set_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expirer', to=settings.AUTH_USER_MODEL)),
                ('finaled_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='finaler', to=settings.AUTH_USER_MODEL)),
                ('issued_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='issuer', to=settings.AUTH_USER_MODEL)),
                ('received_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessory_utility_new_area', models.PositiveIntegerField(default=0)),
                ('residential_dwelling_new_units', models.PositiveIntegerField(default=0)),
                ('residential_dwelling_new_area', models.PositiveIntegerField(default=0)),
                ('assembly_new_area', models.PositiveIntegerField(default=0)),
                ('office_new_area', models.PositiveIntegerField(default=0)),
                ('processing_or_production_new_area', models.PositiveIntegerField(default=0)),
                ('warehouse_new_area', models.PositiveIntegerField(default=0)),
                ('retail_new_area', models.PositiveIntegerField(default=0)),
                ('other_new_area', models.PositiveIntegerField(default=0)),
                ('other_description', models.PositiveIntegerField(default=0)),
                ('building_permit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.bp')),
                ('inspections', models.ManyToManyField(related_name='insps', to='permits.inspectiontype')),
                ('reviews', models.ManyToManyField(related_name='revs', to='permits.inspectiontype')),
            ],
        ),
        migrations.CreateModel(
            name='Demolition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_structures', models.PositiveSmallIntegerField(default=1)),
                ('building_area', models.PositiveIntegerField(default=1000)),
                ('demolition_permit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.bp')),
            ],
        ),
        migrations.CreateModel(
            name='Electrical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phases', models.PositiveIntegerField(default=1)),
                ('voltage', models.PositiveIntegerField(default=240)),
                ('current', models.PositiveIntegerField(default=100)),
                ('service_drop', models.BooleanField(default=False)),
                ('general_lighting_and_receptacles', models.PositiveIntegerField(default=1000)),
                ('pv_solar_roof', models.PositiveIntegerField(default=10)),
                ('pv_solar_ground', models.PositiveIntegerField(default=100)),
                ('evcs', models.PositiveIntegerField(default=100)),
                ('backup_generator', models.PositiveIntegerField(default=100)),
                ('ess_battery', models.PositiveIntegerField(default=100)),
                ('motor_loads', models.PositiveIntegerField(default=100)),
                ('electrical_permit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.bp')),
            ],
        ),
        migrations.CreateModel(
            name='Fire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sprinkler_heads', models.PositiveIntegerField(default=20)),
                ('sprinkler_area', models.PositiveIntegerField(default=2000)),
                ('new_alarm_system', models.BooleanField(verbose_name=False)),
                ('fire_detectors', models.PositiveIntegerField(default=20)),
                ('hazardous_material', models.BooleanField(verbose_name=False)),
                ('high_piled_combustible_storage', models.BooleanField(verbose_name=False)),
                ('fire_protection_permit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.bp')),
            ],
        ),
        migrations.CreateModel(
            name='Flood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bfe', models.PositiveIntegerField(null=True)),
                ('design_depth', models.PositiveIntegerField(null=True)),
                ('FEMA_defined_structure', models.BooleanField(null=True)),
                ('substantial_improvement', models.BooleanField(null=True)),
                ('variance', models.BooleanField(null=True)),
                ('flood_protection_permit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.bp')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.floodzones')),
            ],
        ),
        migrations.CreateModel(
            name='Grading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=20, null=True)),
                ('disturbed_area', models.PositiveIntegerField(default=1000)),
                ('max_cut_depth', models.PositiveIntegerField(default=3)),
                ('max_cut_slope', models.PositiveIntegerField(default=3)),
                ('max_fill_height', models.PositiveIntegerField(default=3)),
                ('max_fill_slope', models.PositiveIntegerField(default=3)),
                ('geotech_report', models.BooleanField(default=True)),
                ('special_inspection', models.BooleanField(default=True)),
                ('grading_permit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.bp')),
            ],
        ),
        migrations.CreateModel(
            name='Mechanical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_units', models.PositiveIntegerField(default=1)),
                ('hvac_units', models.PositiveIntegerField(default=1)),
                ('process_piping', models.PositiveIntegerField(default=1)),
                ('mechanical_permit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.bp')),
            ],
        ),
        migrations.CreateModel(
            name='Plumbing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_supply_service', models.PositiveIntegerField(default=100)),
                ('waste_water_service', models.PositiveIntegerField(default=100)),
                ('general_fixtures', models.PositiveIntegerField(default=1000)),
                ('fuel_gas_appliance', models.PositiveIntegerField(default=1000)),
                ('fuel_gas_pipe', models.PositiveIntegerField(default=1000)),
                ('water_heating_heat_pump', models.PositiveIntegerField(default=100)),
                ('water_heating_solar', models.PositiveIntegerField(default=10)),
                ('water_heating_tankless', models.PositiveIntegerField(default=100)),
                ('plumbing_permit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.bp')),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=100)),
                ('area', models.PositiveIntegerField(default=1000)),
                ('depth', models.PositiveIntegerField(default=6)),
                ('enclosure', models.BooleanField(default=100)),
                ('structural', models.BooleanField(default=100)),
                ('accessibility', models.BooleanField(default=100)),
                ('pool_permit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.bp')),
            ],
        ),
        migrations.CreateModel(
            name='Reroof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reroof_area', models.PositiveIntegerField(default=0)),
                ('fire_class', models.CharField(max_length=1)),
                ('cf1r', models.BooleanField(default=False)),
                ('bp', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='permits_bp.building')),
            ],
        ),
    ]
