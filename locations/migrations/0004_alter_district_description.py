# Generated by Django 5.0 on 2024-01-09 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_alter_siteaddress_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]