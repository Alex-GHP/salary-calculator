from days import *

def get_user_working_days(shifts):
    count = 0
    valid_shifts = ["NORMAL", "MORNING", "LATE", "NIGHT"]
    for shift in shifts[1:]:
        if shift.upper() in valid_shifts:
            count += 1
    return count

def get_day_object(day, shift, hourly_rate):
    weekdays = ["monday", "mondayph", "tuesday", "tuesdayph", "wednesday", "wednesdayph", "thursday", "thursdayph"]

    if day in weekdays:
        return Weekday(day, shift, hourly_rate)
    return WeekendDay(day, shift, hourly_rate)

    
        