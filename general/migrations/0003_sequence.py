# Generated by Django 5.0 on 2024-01-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_alter_tag_policy_alter_taggedrecord_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=7)),
                ('year', models.DateTimeField(default='2024')),
                ('sequence', models.IntegerField()),
                ('description', models.TextField(max_length=255)),
            ],
        ),
    ]