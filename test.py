import calendar
import datetime
from datetime import date

# Get the current date
current_date = datetime.datetime.now()

# Set the day to the 2nd
second_day = current_date.replace(day=1)

# Get the day of the week as an integer (0 = Monday, 6 = Sunday)
day_of_week = second_day.weekday()

# Get the name of the day using the calendar module
day_name = calendar.day_name[day_of_week]

print(f"The name of the 2nd day of the month is: {day_name}")


current_day = date.today()
day_order = []
day_numbers = []
month_number = []

month_lenght = calendar.monthrange(date.today().year, date.today().month)
current_day_name =  calendar.day_name[current_day.weekday()]
first_day_name =  calendar.day_name[month_lenght[0]]

for days in range(month_lenght[1]):
    day_order.append(calendar.day_name[current_date.replace(day=days+1).weekday()])
    day_numbers.append(days+1)
    month_number.append(date.today().month)

print(day_order)

if (day_order[0] != 'Monday'):
    previous_month = current_date.replace(month=date.today().month-1)
    last_day_previous_month = calendar.monthrange(previous_month.year, previous_month.month)[1]
    print(previous_month.month, date.today().month, last_day_previous_month)

    i = 0
    while day_order[0] != 'Monday':
        day_order.insert(0, calendar.day_name[previous_month.replace(day=last_day_previous_month-i).weekday()])
        day_numbers.insert(0, last_day_previous_month-i)
        month_number.insert(0, previous_month.month)
        i += 1
        
print(day_order)
print(day_numbers)
print(month_number)

