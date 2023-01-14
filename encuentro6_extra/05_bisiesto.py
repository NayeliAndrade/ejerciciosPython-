"""Make a program that, given a year, tells us whether it is a leap year or not. A year is a leap year under 
the following conditions: A year divisible by 4 is a leap year and must not be divisible by 100. 
If a year is divisible by 100 and is also divisible by 400, it is also leap year"""

year = int(input("Enter the year: "))

if year % 4 == 0 and year % 100!=0: 
    print("year is leap")

elif year % 100 == 0 and year % 400 == 0:
    print("is leap")
else:
    print("error")
