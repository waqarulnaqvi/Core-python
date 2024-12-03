# Assignment 11
# Problem :1
import datetime

current_datetime=datetime.datetime.now()
print("Current date and time: ",current_datetime)

current_year=current_datetime.year
print("Current year: ",current_year)

month_of_year=current_datetime.strftime("%B")
print("Current month: ",month_of_year)

week=current_datetime.strftime("%U")
print("Week number of the year: ",week)

weekday=current_datetime.strftime("%A")
print("Weekday of the week: ",weekday)

day_of_year=current_datetime.strftime("%j")
print("Day of year:",day_of_year)

day_of_month=current_datetime.strftime("%d")
# day_of_month=current_datetime.day
print("Day of the month:",day_of_month)

day_of_week=current_datetime.strftime("%w")
print("Day of week: ",day_of_week)

# Problem :2
# inp=int(input("Enter a year:"))
# if inp%4==0 and (inp%100!=0 or inp%400==0  ):
#     print("It's a leap year!!")
# else:
#     print("It's not a leap year!!")

# Problem :3
# import datetime
# current_datetime=datetime.datetime.now()
# current_time=current_datetime.time()
# print("Current time: ",current_time)

# Problem:4
import datetime
current_datetime=datetime.datetime.now()
milli_second=current_datetime.microsecond
print("Current time in milli second: ",milli_second)

# Problem:5
import datetime
current_datetime=datetime.datetime.now()
week=current_datetime.strftime("%U")
print("Week number of the year: ",week)

# Question 6: Write a Python program to get the week number.

import datetime

# Get the current date
current_date = datetime.datetime.now()

# Extract the week number from the current date
week_number = current_date.strftime("%U")

# Print the week number
print("Week number:", week_number)


# Question 7: Write a Python program to print a string five times, with a delay of three seconds.

import time

# Function to print a string five times with a delay of three seconds
def print_string():
    for i in range(5):
        print("Hello, world!")
        time.sleep(3)

# Call the function to print the string
print_string()


# Question 8: Write a Python program to generate a date and time as a string.

import datetime

# Generate the current date and time as a string
current_datetime = datetime.datetime.now()

# Format the current date and time as a string
datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Print the date and time string
print("Current date and time:", datetime_string)


# Problem:9
import datetime

current_datetime=datetime.datetime.now()

year_month=current_datetime.strftime("%Y %B")
print("Current month: ",year_month)