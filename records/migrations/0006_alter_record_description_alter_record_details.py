# Generated by Django 5.0 on 2024-01-16 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_alter_type_division_alter_type_policy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='description',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AlterField(
            model_name='record',
            name='details',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
