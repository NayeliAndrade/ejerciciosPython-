"""Make an algorithm that reads a number from the keyboard and determines if it has three digits."""

num = str(input("Enter the number: "))

validation = len(num)
#print(validacion)

if validation == 3:
    print("There are 3 digits")
elif validation <3:
    print("has less than 3 digits")
elif validation >3:
    print("has more than 3 digits")
