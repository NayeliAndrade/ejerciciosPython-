"""Read three numbers denoting a date (day, month, year) and check that it is a valid date.
If the date is not valid, write an error monthsage on the screen. If the date is valid 
print the date by changing the number representing the month by its name. For example: if you 
1 2 2006 is entered, "February 1, 2006" should be printed.  """

day = int(input("enter day: "))

month = int(input("enter month: "))

year = int(input("enter year: "))

if day > 1 and day < 32: 
    if month == 1: 
        print("The date is ", day, "January", year)
    elif month == 2:
	    print("The date is ", day, "february", year)
    elif month == 3:
        print("The date is ", day, "march", year)
    elif month == 4:
        print("The date is ", day, "april", year)
    elif month == 5:
        print("The date is ", day, "may", year)
    elif month == 6:
        print("The date is ", day, "june", year)
    elif month == 7:
        print("The date is ", day, "july", year)
    elif month == 8:
        print("The date is ", day, "august", year)
    elif month == 9:
        print("The date is ", day, "september", year)
    elif month == 10:
        print("The date is ", day, "october", year)
    elif month == 11:
        print("The date is ", day, "november", year)
    elif month == 12:
        print("The date is ", day, "december", year)
    else:
        print("El month to enter does not exist")
else:
    print("the date does not exist")