"""Ask the user to enter a value between 1 and 7. The program should display a message 
display a message indicating which day of the week it corresponds to. Consider that the number 
1 corresponds to "Monday", and so on. """

day = int(input("enter a number from 1 to 7 to find out which day it corresponds to: "))

if day == 1:
    print("Monday")
elif day == 2:
     print("Tuesday")
elif day == 3:
     print("Wednesday")
elif day == 4:
     print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
     print("Saturday")
elif day == 7:
     print("Sunday")
else:
    print("No exist")

