# Write a function that calculate the perimeter of a circle using pi from the math library.
# Tips : perimeter = 2 * 𝜋 * radius 
from math import pi

def circle_perimeter(radius):
    return 2 * pi * radius
input_radius = float(input("Enter the radius of the circle: "))
print(f"The perimeter of the circle is {circle_perimeter(input_radius)}")

# Create a function that returns today's date + one week.
from datetime import datetime, timedelta

def date_plus_one_week():
    return datetime.now() + timedelta(weeks=1)

print(f"Today is {datetime.now().strftime('%Y-%m-%d')} and in one week it will be {date_plus_one_week().strftime('%Y-%m-%d')}")

# Create a program that asks the user for an offset (in hours) from UTC (GMT+0) 
# and returns the current date and time in the corresponding time zone.
from datetime import datetime, timedelta

def current_time_with_offset(offset_hours):
    return datetime.utcnow() + timedelta(hours=offset_hours)
offset = int(input("Enter the offset from UTC in hours: "))
print(f"The current date and time in the specified time zone is: {current_time_with_offset(offset).strftime('%Y-%m-%d %H:%M:%S')}")
1