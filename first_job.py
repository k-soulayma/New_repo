import os
from datetime import datetime

env_date = os.getenv("INPUT_DATE")

if env_date:
    try:
        input_date = datetime.strptime(env_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format")
        exit()

    actual_date = datetime.today().date()

    if input_date == actual_date:
        print("Yes, today is ", actual_date)
    else:
        print("Today is not", input_date, " it is", actual_date)
else:
    print("No date provided.")
