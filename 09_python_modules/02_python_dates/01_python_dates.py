#Python Dates

# A date in python is not a data type but we can import date module <datetime> to work with dates as date object.

import datetime as date

x = date.datetime.now()
print(x) #2023-11-16 21:40:10.764570

# The date contains year, month, day, hour, minute, second, and microsecond.
# datetime module has many methods to return information about the date object. 

print(x.year)
print(x.strftime("%A"))
print(x.strftime("%d-%m-%Y"))

#Creating Date Object
# to create a date, we can use datetime() class constructor of <datetime> module
# datetime() class required three parameters to create a date: year, month and day.

y = date.datetime(2020,5,2)
print(y)

#strftime() method
# formats the date object into readable strings
# takes in one parameter, to specify the format of the returned string.

print(y.strftime("%B"))