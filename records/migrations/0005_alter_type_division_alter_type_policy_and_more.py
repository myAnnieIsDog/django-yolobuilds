# Generated by Django 5.0 on 2024-01-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_alter_number_options_type_division_type_prefix_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='division',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='policy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='prefix',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='suffix',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
