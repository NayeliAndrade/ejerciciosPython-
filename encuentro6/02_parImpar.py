"""Create a program that, given an integer, displays on the screen whether it is even or odd. 
If the value entered is 0, "the number is neither odd nor even" must be displayed."""

num = int(input("Enter a number: "))

if num % 2 == 0: 
    print("the number is even")
elif num == 0: 
    print("the number is neither odd nor even")
else:
    print("The number is odd")