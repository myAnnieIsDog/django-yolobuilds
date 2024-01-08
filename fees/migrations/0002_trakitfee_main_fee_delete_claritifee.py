# Generated by Django 5.0 on 2024-01-07 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trakitfee',
            name='main_fee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='trakit_fee', to='fees.fee'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ClaritiFee',
        ),
    ]
