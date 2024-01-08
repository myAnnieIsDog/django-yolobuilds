# Generated by Django 5.0 on 2024-01-05 14:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=55, unique=True)),
                ('requirements', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Inspection Result Option',
                'verbose_name_plural': 'Inspection Result Options',
            },
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_time_allotted', models.DecimalField(decimal_places=1, max_digits=7)),
                ('staff_time_actual', models.DecimalField(decimal_places=1, max_digits=7)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inspections.inspectionresult')),
            ],
        ),
        migrations.CreateModel(
            name='InspectionTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resulted', models.DateTimeField(null=True)),
                ('inspector', models.CharField(blank=True, max_length=100, null=True)),
                ('time_allotted', models.DecimalField(decimal_places=1, max_digits=7)),
                ('time_actual', models.DecimalField(decimal_places=1, max_digits=7)),
                ('time_delta', models.DecimalField(decimal_places=1, max_digits=7)),
                ('scheduled_date', models.DateField()),
                ('scheduled_time', models.TimeField()),
                ('requested_by', models.CharField(blank=True, max_length=100, null=True)),
                ('requested_date', models.DateField()),
                ('requested_notes', models.CharField(blank=True, max_length=256, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inspections.inspection')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inspections.inspectionresult')),
            ],
            options={
                'verbose_name': 'Inspection Trip',
                'verbose_name_plural': 'Inspection Trips',
            },
        ),
        migrations.CreateModel(
            name='InspectionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_type', models.CharField(max_length=30)),
                ('duration_hours', models.DecimalField(decimal_places=1, default=0.3, max_digits=3)),
                ('trip_factor', models.DecimalField(decimal_places=2, default=1.2, max_digits=7)),
                ('inspection_checklist', models.TextField(blank=True)),
                ('add_next', models.ManyToManyField(blank=True, to='inspections.inspectiontype')),
                ('default_inspector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Inspection Type',
                'verbose_name_plural': 'Inspection Types',
            },
        ),
    ]
