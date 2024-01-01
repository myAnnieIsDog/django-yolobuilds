import csv  # https://docs.python.org/3/library/csv.html
from django.db.utils import IntegrityError
from fees.models import Fund, BudgetUnit, FeeType

##########################################################################
""" Run this script using the following terminal command:
        python manage.py runscript fees_init        """
##########################################################################

tables = ()
base = "scripts/init/"

def run():
    print(funds())
    print(units())
    print(fees())


##########################################################################
""" Initial Account Data """
##########################################################################


def funds():
    g, x, y = 0, 0, 0
    with open(f'{base}fiscal_funds.csv', newline="") as f:
        f.readline()
        spam = csv.reader(f, dialect="excel")
        for row in spam:
            try:
                a = Fund()
                a.fund_label = row[0]
                a.fund_id = row[1]
                a.fund_description = row[2]
                a.save()
                g += 1
            except IntegrityError:
                x += 1
            except:
                y += 1
    return f"'Funds' complete. {g} successful. {x} duplicates. {y} errors."


def units():
    g, x, y = 0, 0, 0
    with open(f'{base}fiscal_budget_unit.csv', newline="") as f:
        f.readline()
        spam = csv.reader(f, dialect="excel")
        for row in spam:
            try:
                a = BudgetUnit()
                a.unit=row[0], 
                a.unit_label=row[1],
                a.unit_description=row[2],
                a.save()
                g += 1
            except IntegrityError:
                x += 1
            except:
                y += 1
    return f"'Budget Units' complete. {g} successful. {x} duplicates. {y} errors."


##########################################################################
""" Initial Fee Data """
##########################################################################

def fees():
    g, x, y = 0, 0, 0
    with open(f'{base}fiscal_fees.csv', newline="") as f:
        f.readline()
        spam = csv.reader(f, dialect="excel")
        for row in spam:
            try:
                a = FeeType()
                a.fee_type=row[0]
                a.policy=row[1]
                a.authorization=row[2]
                # a.adopted=row[3]
                # a.revised=row[4]
                # a.expires=row[5]
                
                a.tier_base_qty=row[6]
                a.tier_base_fee=row[7]
                a.rate=row[8]
                a.units=row[9]
                a.rate_check=row[10]

                # a.budget_unit_1=row[11],
                a.budget_unit_1_share=row[12]
                # a.budget_unit_2=row[13],
                a.budget_unit_2_share=row[14]
                a.save()
                g += 1
            except IntegrityError:
                x += 1
            except:
                y += 1
    return f"'Fee Types' complete. {g} successful. {x} duplicates. {y} errors."


##########################################################################
""" End File """
##########################################################################