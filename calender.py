"""Problem:- Write a Python program to print the calendar of a given month and year (Use
‘calendar’ module"""

import calendar
cho=int(input("1.Entire year\n2.A month\nEnter your choice:-"))
if(cho==1):
    y=int(input("Enter the year:-"))
    print(calendar.calendar(y))
elif(cho==2):
    y = int(input("Enter the year:-"))
    m=int(input("Enter the number of month:-"))
    print(calendar.month(y,m))
else:
    print("Wrong input")