import csv

from constants import BASE_SALARY, PAID_HOURS_PER_SHIFT, WEEKEND_DAYS
from get_work_days import get_user_working_days


with open("Schedule - 2025.csv", mode="r") as file:
    reader = csv.reader(file)

    days = next(reader)
    shifts = next(reader)


work_days = len(days) - 1 - WEEKEND_DAYS
user_working_days = get_user_working_days(shifts)

print(user_working_days)

total_salary = 0
for day in days[1:]:
    work_day = get_day_object(day)
    total_salary += work_day.get_money()

daily_rate = BASE_SALARY // work_days
hourly_rate = daily_rate / PAID_HOURS_PER_SHIFT

def get_hours(day, shift):
    pass





