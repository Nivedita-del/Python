'''Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. '''
import calendar
a = int(input("month"))
b = int(input("year"))
print(calendar.month(b,a))
