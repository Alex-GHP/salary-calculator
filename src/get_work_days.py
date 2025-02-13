from constants import MIN_LEGAL_WORK_DAYS, MAX_LEGAL_WORK_DAYS, WEEKEND_DAYS
import csv

def get_user_working_days(shifts):
    count = 0
    valid_shifts = ["NORMAL", "MORNING", "LATE", "NIGHT"]
    for shift in shifts[1:]:
        if shift.upper() in valid_shifts:
            count += 1
    return count

    
        