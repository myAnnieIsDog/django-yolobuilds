import os
from django.core import serializers

##########################################################################
""" python manage.py runscript import_yaml """
##########################################################################
def run():
    directory = os.fsencode("scripts/init/")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".yaml"):
            for obj in serializers.deserialize("yaml", file):
                obj.save()
