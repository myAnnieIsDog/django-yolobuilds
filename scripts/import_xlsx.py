import json
from django.core import serializers
from django.db import IntegrityError

# from django_pandas.io import read_frame
# from django_pandas.managers import DataFrameManager
# from django_pandas.models import 
# from django_pandas.tests import 
# from django_pandas.utils import 
import pandas as pd

from fees.models import Account, FeeType, PaymentMethod
from inspections.models import InspectionType, InspectionResult
from locations.models import District, Jurisdiction
from permits.models import Tag, Division, PermitStatus, PermitType, Sequence
from permits_bp.models import ApplicantRole, OwnerRole
from profiles.models import Profile, LicenseAgency, LicenseType, Agency, Department, Division, Staff
from reviews.models import ReviewType, ReviewStatus, CycleResult

##########################################################################
""" python manage.py runscript import_xlsx """
##########################################################################

base = ".init/"
library = [
    ["fiscal", "accounts", Account],
    ["fiscal", "fee_types", FeeType],
    ["fiscal", "payment_methods", PaymentMethod],

    ["inspections", "insp_type", InspectionType],
    ["inspections", "insp_result", InspectionResult],

    ["locations", "districts", District],
    ["locations", "jurisdictions", Jurisdiction],

    ["permits", "sequence", Sequence],
    ["permits", "tags", Tag],
    ["permits", "permit_status", PermitStatus],
    ["permits", "permit_type", PermitType],
    ["permits", "app_role", ApplicantRole],
    ["permits", "owner_role", OwnerRole],
    # ["permits", "sequence", Sequence],

    ["profiles", "agency", Agency],
    ["profiles", "department", Department],
    ["profiles", "division", Division],
    ["profiles", "profile", Profile],
    ["profiles", "licenser", LicenseAgency],
    ["profiles", "license_type", LicenseType],

    ["reviews", "review_type", ReviewType],
    ["reviews", "review_status", ReviewType],
    ["reviews", "cycle_result", ReviewType],
]

def run():
    for i in library:
        core_func(i[0], i[1], i[2])


def core_func(app, sheet, model):
    spam = pd.read_excel(
        f'{base}{app}.xlsx', 
        engine="openpyxl",
        sheet_name=sheet,
        index_col=0,
    )
    
    fields = pd.DataFrame.to_csv(spam, lineterminator="\r") # f"{base}json/{app}_{sheet}.json",
    with open(f"{base}csv/{app}_{sheet}.csv", "x") as f:
        f.write(fields)
        print(f)
    
    # item_id = 6
    # item = [
    #     {"pk": f"{item_id}"},
    #     {"model": f"{app}.{model}"},
    #     {"fields": fields},
    # ]
    # jason = json.dumps(item)
    

    # # for obj in serializers.deserialize("json", jason):
    # #     obj.save()
    # print(str(model))


    # print(spam)
    # g = 0
    # x = 0
    # y = 0
    # for row in spam:
    #     a = model()
    #     try:
    #         for key, value in row.items():
    #             print(key, value)
    #             a.row = value
    #             a.save()
    #         g += 1
    #     except IntegrityError:
    #         x += 1
    #     except:
    #         y += 1
    # print(f"{model}: {g} written, {x} duplicates, {y} errors.")

            


# def funds():
#     g, x, y = 0, 0, 0
#     with open(f'{base}fiscal_funds.csv', newline="") as f:
#         f.readline()
#         spam = csv.reader(f, dialect="excel")
#         
#     return f"'Funds' complete. {g} successful. {x} duplicates. {y} errors."


# def units():
#     g, x, y = 0, 0, 0
#     with open(f'{base}fiscal_budget_unit.csv', newline="") as f:
#         f.readline()
#         spam = csv.reader(f, dialect="excel")
#         for row in spam:
#             try:
#                 a = BudgetUnit()
#                 a.unit=row[0], 
#                 a.unit_label=row[1],
#                 a.unit_description=row[2],
#                 a.save()
#                 g += 1
#             except IntegrityError:
#                 x += 1
#             except:
#                 y += 1
#     return f"'Budget Units' complete. {g} successful. {x} duplicates. {y} errors."


# ##########################################################################
# """ Initial Fee Data """
# ##########################################################################

# def fees():
#     g, x, y = 0, 0, 0
#     with open(f'{base}fiscal_fees.csv', newline="") as f:
#         f.readline()
#         spam = csv.reader(f, dialect="excel")
#         for row in spam:
#             try:
#                 a = FeeType()
#                 a.fee_type=row[0]
#                 a.policy=row[1]
#                 a.authorization=row[2]
#                 # a.adopted=row[3]
#                 # a.revised=row[4]
#                 # a.expires=row[5]
                
#                 a.tier_base_qty=row[6]
#                 a.tier_base_fee=row[7]
#                 a.rate=row[8]
#                 a.units=row[9]
#                 a.rate_check=row[10]

#                 # a.budget_unit_1=row[11],
#                 a.budget_unit_1_share=row[12]
#                 # a.budget_unit_2=row[13],
#                 a.budget_unit_2_share=row[14]
#                 a.save()
#                 g += 1
#             except IntegrityError:
#                 x += 1
#             except:
#                 y += 1
#     return f"'Fee Types' complete. {g} successful. {x} duplicates. {y} errors."


# ##########################################################################
# """ End File """
# ##########################################################################