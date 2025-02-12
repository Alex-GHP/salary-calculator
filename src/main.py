from constants import MAX_LEGAL_WORK_DAYS

while True:
    print("Enter the number of worked days: ", end="")
    num_days_worked: int = input()
    try:
        num_days_worked = int(num_days_worked)
    except:
        print("Please use numeric digits")
        continue
    if num_days_worked < 0:
        print("Please enter a positive number")
        continue
    if num_days_worked > MAX_LEGAL_WORK_DAYS:
        print(f"The maximum number of legal working days in Romania is {MAX_LEGAL_WORK_DAYS}.")
    break 