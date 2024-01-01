# Generated by Django 5.0 on 2023-12-31 14:40

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0004_alter_feetype_rate_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feetype',
            name='budget_unit_1',
        ),
        migrations.RemoveField(
            model_name='feetype',
            name='budget_unit_1_share',
        ),
        migrations.RemoveField(
            model_name='feetype',
            name='budget_unit_2',
        ),
        migrations.RemoveField(
            model_name='feetype',
            name='budget_unit_2_share',
        ),
        migrations.AddField(
            model_name='feetype',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='feetype',
            name='budget_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fees.budgetunit'),
        ),
        migrations.AddField(
            model_name='feetype',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feetype',
            name='rate',
            field=models.FloatField(default=5000000),
        ),
        migrations.AlterField(
            model_name='feetype',
            name='tier_base_fee',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='feetype',
            name='tier_base_qty',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='feetype',
            name='units',
            field=models.CharField(default='each', max_length=255),
        ),
        migrations.CreateModel(
            name='UIGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=5)),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fees.budgetunit')),
            ],
            options={
                'verbose_name': 'UI Group',
                'verbose_name_plural': 'UI Groups',
            },
        ),
        migrations.AddField(
            model_name='feetype',
            name='fee_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fees.uigroup'),
        ),
        migrations.CreateModel(
            name='UnitPortion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share', models.DecimalField(decimal_places=2, default=1.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('fee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='fees.feetype')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='fees.budgetunit')),
            ],
            options={
                'verbose_name': 'Budget Unit Portion',
                'verbose_name_plural': 'Budget Unit Portions',
            },
        ),
    ]