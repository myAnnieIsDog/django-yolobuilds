from django.core import serializers
from django.utils import timezone

##########################################################################
""" python manage.py runscript bak_yaml """
##########################################################################
from fees.models import all_models as fee_models
from inspections.models import all_models as inspections_models

model_lists = [
    fee_models,
    inspections_models,
]

def run():
    for list in model_lists:
        yaml_backup(list)

def yaml_backup(model_list):
    date = str(timezone.localdate())
    time = str(timezone.localtime())
    for model in model_list:
        data = serializers.serialize("yaml", model.objects.all())
        with open(f".db_backup/{str(model._meta.model_name)} {date}.yaml", "w") as f:
            f.write(data)
            f.close()
    return True
