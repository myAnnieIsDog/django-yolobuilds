""" This script controls the database backup system. """
import datetime as dt

def run():
    which_list()

def which_list():
    today = dt.datetime.now()
    year = today.year
    month = today.month
    weekday = today.weekday
    day = today.day
    # if month == 1 and day == 1:
    #     bak_annual(year)
    # if day == 1 and (month == 4 or month == 7 or month == 10):
    #     bak_quarter(today)
    # if day == 1:
    #     bak_monthly(today)
    # if weekday == 4:
    #     bak_weekly(today)
    # else:
    bak_daily(today)

def bak_daily():
    pass
    # Write a script to create a daily backup, erasing backup older than 3 days.

def bak_weekly():
    pass
    # Write a script to create a weekly backup, erasing backup older than 3 weeks.

def bak_monthly():
    pass
    # Write a script to create a weekly backup, erasing backup older than 3 weeks.


if __name__ == '__main__':
    run()