import csv

from constants import BASE_SALARY, PAID_HOURS_PER_SHIFT, WEEKEND_DAYS
from get_work_days import get_user_working_days, get_day_object
from days import *


with open("Schedule - 2025.csv", mode="r") as file:
    reader = csv.reader(file)

    days = next(reader)
    shifts = next(reader)


work_days = len(days) - 1 - WEEKEND_DAYS
user_working_days = get_user_working_days(shifts)

print(days)
print(shifts)

daily_rate = BASE_SALARY // work_days
hourly_rate = daily_rate / PAID_HOURS_PER_SHIFT

total_salary = 0
for i in range(1, len(days)):
    if shifts[i] == "OFF":
        continue
    work_day = get_day_object(days[i], shifts[i], hourly_rate)
    if "ph" in work_day.day:
        total_salary += work_day.get_money() * 2
    total_salary += work_day.get_money()

print(total_salary)







