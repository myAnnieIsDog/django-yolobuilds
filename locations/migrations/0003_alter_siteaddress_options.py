# Generated by Django 5.0 on 2024-01-09 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_alter_parcel_related'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='siteaddress',
            options={'verbose_name': 'Site Address', 'verbose_name_plural': 'Site Addresses'},
        ),
    ]