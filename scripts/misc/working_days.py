from calendar import weekday
from datetime import date
from datetime import timedelta as delta
from pickle import dump, load


def main():
    forecast_start = date.today()
    forecast_length = 365
    business_days = []
    with open("py/business_days.pickle", "rb") as f:
        business_days = load(f)

    for i in range(forecast_length):
        testdate = forecast_start + delta(days=i)
        day_of_week = weekday(testdate.year, testdate.month, testdate.day)
        if day_of_week == 5: 
            business_days.append(f"{testdate} is Saturday")
            continue
        if day_of_week == 6: 
            business_days.append(f"{testdate} is Sunday")
            continue
        else: 
            business_days.append(f"{testdate} is {holiday(testdate, day_of_week)}")
    
    business_days = sorted(list(set(business_days)))

    with open("py/business_days.pickle", "wb") as f:
        dump(business_days, f)

    with open("py/business_days.txt", "w") as f:
        for i in business_days:
            f.write(f"{i}\n")


def holiday(testdate, day_of_week):
    holidays = {
        "01-01": "New Year's Day", # also check for Mon Jan 2 New Year
        "03-31": "Martin Luther King Jr Day", # also check for Mon 04-01 and Fri 03-30 Cesar Chavez
        "06-19": "Juneteenth", # also check for Mon 06-20 and Fri 06-18 Juneteenth
        "07-04": "Independence Day", # also check for Mon 07-05 and Fri 07-03 Independence
        "11-11": "Veteran's Day", # also check for Mon 11-12 and Fri 11-10 Veteran's

        "12-25": "Christmas", # also check for Fri 12-24 Christmas
        "12-26": "Winter Break", # Winter break
        "12-27": "Winter Break", # Winter break
        "12-28": "Winter Break", # Winter break
        "12-29": "Winter Break", # Winter break
        "12-30": "Winter Break", # Winter break
        "12-31": "Winter Break", # Winter break
    }

    mondays = {
        "01-02": "New Year's Day (observed)", # if New Year is a Sunday

        "01-15": "Martin Luther King Jr Day", 
        "01-16": "Martin Luther King Jr Day", 
        "01-17": "Martin Luther King Jr Day", 
        "01-18": "Martin Luther King Jr Day", 
        "01-19": "Martin Luther King Jr Day", 
        "01-20": "Martin Luther King Jr Day", 
        "01-21": "Martin Luther King Jr Day", # MLK (third Monday in Jan)

        "02-15": "President's Day", 
        "02-16": "President's Day", 
        "02-17": "President's Day", 
        "02-18": "President's Day", 
        "02-19": "President's Day", 
        "02-20": "President's Day", 
        "02-21": "President's Day", # Presidents (third Monday in Feb)

        "04-01": "Cesar Chavez Day (observed)", # if Cesar Chavez is a Sunday

        "05-25": "Memorial Day", 
        "05-22": "Memorial Day", 
        "05-27": "Memorial Day", 
        "05-28": "Memorial Day", 
        "05-29": "Memorial Day", 
        "05-30": "Memorial Day", 
        "05-31": "Memorial Day", # Memorial (last Monday in May)

        "06-20": "Juneteenth (observed)", # if Juneteenth is a Sunday
        "07-05": "Independence Day (observed)", # if Independence Day is a Sunday

        "09-01": "Labor Day", 
        "09-02": "Labor Day", 
        "09-03": "Labor Day", 
        "09-04": "Labor Day", 
        "09-05": "Labor Day", 
        "09-06": "Labor Day", 
        "09-07": "Labor Day", # Labor (first Monday in Sep)

        "11-12": "Veteran's Day (observed)", # if Veteran's Day is a Sunday
    }
    thursdays = {
        "11-22": "Thanksgiving Day", 
        "11-23": "Thanksgiving Day", 
        "11-24": "Thanksgiving Day", 
        "11-25": "Thanksgiving Day", 
        "11-26": "Thanksgiving Day", 
        "11-27": "Thanksgiving Day", 
        "11-28": "Thanksgiving Day", # Thanksgiving (fourth Thursday in Nov)
    }

    fridays = {
        "03-30": "Cesar Chavez Day (observed)", # if Cesar Chavez is a Saturday
        "06-18": "Juneteenth (observed)", # if Juneteenth is a Saturday
        "07-03": "Independence Day (observed)", # if Independence Day is a Saturday
        "11-10": "Veteran's Day (observed)", # if Veteran's Day is a Saturday

        "11-23": "Day After Thanksgiving", 
        "11-24": "Day After Thanksgiving", 
        "11-25": "Day After Thanksgiving", 
        "11-26": "Day After Thanksgiving", 
        "11-27": "Day After Thanksgiving", 
        "11-28": "Day After Thanksgiving", 
        "11-29": "Day After Thanksgiving", # Day after Thanksgiving (fourth Friday in Nov)

        "12-24": "Christmas Day (observed)", # if Christmas is a Saturday
    }

    date2check = f"{testdate.month}-{testdate.day}"
    if date2check in holidays:
        return holidays[date2check]
    elif (day_of_week == 0) & (date2check in mondays):
        return mondays[date2check]
    elif (day_of_week == 3) & (date2check in thursdays):
        return thursdays[date2check]
    elif (day_of_week == 4) & (date2check in fridays):
        return fridays[date2check]
    else:
        return "a Business Day"


if __name__ == "__main__":
    main()
