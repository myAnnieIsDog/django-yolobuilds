# Generated by Django 5.0 on 2024-01-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='related',
            field=models.ManyToManyField(blank=True, to='locations.parcel'),
        ),
    ]
