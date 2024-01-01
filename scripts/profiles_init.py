import csv  # https://docs.python.org/3/library/csv.html
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from profiles.models import (
    Profile, LicenseAgency, LicenseType,
    AgencyOptions, DepartmentOptions, DivisionOptions,
)

##########################################################################
""" Run this script using the following terminal command:
        python manage.py runscript profiles_init        """
##########################################################################


base = "scripts/init/"

def run():
    print(agencies())
    print(departments())
    print(divisions())
    print(license_agencies())
    print(license_types())
    print(profiles())


##########################################################################
""" Initial Profile Data """
##########################################################################


def agencies():
    g, x, y = 0, 0, 0
    with open(f'{base}profiles_agencies.csv', newline="") as f:
        f.readline()
        spam = csv.reader(f, dialect="excel")
        for row in spam:
            try:
                a = AgencyOptions()
                a.agency_option_short = row[0]
                a.agency_option_full = row[1]
                a.save()
                g += 1
            except IntegrityError:
                x += 1
            except:
                y += 1
    return f"'Agencies' complete. {g} successful. {x} duplicates. {y} errors."


def departments():
    g, x, y = 0, 0, 0
    with open(f'{base}profiles_departments.csv', newline="") as f:
        f.readline()
        spam = csv.reader(f, dialect="excel") 
        for row in spam:
            try:
                d = DepartmentOptions()
                d.department_option_short = row[0]
                d.department_option_full = row[1]
                d.save()
                g += 1
            except IntegrityError:
                x += 1
            except:
                y += 1
    return f"'Departments' complete. {g} successful. {x} duplicates. {y} errors."


def divisions():
    g, x, y = 0, 0, 0  
    with open(f'{base}profiles_divisions.csv', newline="") as f:
        f.readline()
        spam = csv.reader(f, dialect="excel")
        for row in spam:
            try:
                d = DivisionOptions()
                d.division_options = row[0]
                d.save()
                g += 1
            except IntegrityError:
                x += 1
            except:
                y += 1
    return f"'Divisions' complete. {g} successful. {x} duplicates. {y} errors."


##########################################################################
""" Initial License Data """
##########################################################################


def license_agencies():
    g, x, y = 0, 0, 0
    with open(f'{base}profiles_license_agencies.csv', newline="") as f:
        f.readline()
        spam = csv.reader(f, dialect="excel")
        for row in spam:
            try:
                l = LicenseAgency()
                l.agency_short = row[0]
                l.agency_long = row[1]
                l.save()
                g += 1
            except IntegrityError:
                x += 1
            except:
                y += 1
    return f"'License Agencies' complete. {g} successful. {x} duplicates. {y} errors."


def license_types():
    g, x, y = 0, 0, 0 
    with open(f'{base}profiles_license_types.csv', newline="") as f:
        f.readline()
        spam = csv.reader(f, dialect="excel")
        for row in spam:
            try:
                l = LicenseType()
                l.license_short=row[0]
                l.license_long=row[1]
                l.save()
                g += 1
            except IntegrityError:
                x += 1
            except:
                y += 1
    return f"'License Type' complete. {g} successful. {x} duplicates. {y} errors."


##########################################################################
""" Initial Profile Data """
##########################################################################


def profiles():
    Profile.objects.all().delete()
    g, x, y = 0, 0, 0  
    with open(f'{base}profiles.csv', newline="") as f:
        f.readline()
        spam = csv.reader(f, dialect="excel")
        for row in spam:
            try:
                # u = User()
                # u.username = row[0]
                # u.first_name = row[1]
                # u.last_name = row[2]
                # u.email = row[3]
                # u.is_active = row[4]
                # u.is_staff = row[5]
                # u.is_superuser = row[6]
                # u.set_unusable_password
                # u.save()

                p = Profile()
                # p.user = u.id
                p.first = row[1]
                p.last = row[2]
                p.email = row[3]
                p.company_name = row[7]
                p.phone_number = row[8]
                p.address = row[9]
                p.city = row[10]
                p.state = row[11]
                p.zip = row[12]
                p.save()
                g += 1
            except Exception as e:
                print(e)
    return f"'Profile' complete. {g} successful. {x} duplicates. {y} errors."


##########################################################################
""" End File """
##########################################################################