from django.core import serializers
# from fees.models import Fund
from fees.models import Fund, BudgetUnit, FeeType
# from general.models import all_models as general
# from inspections.models import all_models as inspections
# from locations.models import all_models as locations
# from payments.models import all_models as payments
# from permits.models import all_models as permits
# from permits_bp.models import all_models as permits_bp
# from profiles.models import all_models as profiles
# from reviews.models import all_models as reviews
from django.utils import timezone

##########################################################################
""" python manage.py runscript serialize """
##########################################################################
def run():
    # Must include parent models. Include all non-abstrat models.
    model_list = [Fund, BudgetUnit, FeeType]
    # Extend to include "all_models" from each app.
    # model_list.extend(fees)
    # model_list.extend(general)
    # model_list.extend(inspections)
    # model_list.extend(locations)
    # model_list.extend(payments)
    # model_list.extend(permits)
    # model_list.extend(permits_bp)
    # model_list.extend(profiles)
    # model_list.extend(reviews)

    format_list = (
        "xml",
        "json",
        "jsonl",
        "yaml",
    )

    print(yaml_backup(model_list))


def yaml_backup(model_list):
    now = str(timezone.now())
    for model in model_list:
        data = serializers.serialize("yaml", model.objects.all())
        with open(f".db_backup/{str(model._meta.model_name)}.yaml", "w") as f:
            f.write(data)
            f.close()
    return True

    # now = timezone.now()
    # for i in model_list:
    #     instances = 
    #     data = serializers.serialize(format, i.objects.all())
    #     with open(f"/.db_backup/{i.__str__()}.xml", "w") as f:
    #         f = data
    #         f.save()


if __name__ == "__main__":
    run()
