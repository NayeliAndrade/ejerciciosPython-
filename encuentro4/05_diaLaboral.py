#5
"""Create an application that asks us for a day of the week and tells us if it is a working day or not.  """

day = input("enter a day of the week: ")

if day == "saturday" or day == "sunday":
    print("No work on this day")
else: 
    print("This day you go to work")