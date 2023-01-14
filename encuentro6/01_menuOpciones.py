"""Build a program that simulates a menu of options to perform the four basic arithmetic operations (addition, 
subtraction, multiplication and division) with two integer numerical values. 
arithmetic operations (addition, subtraction, multiplication and division) with two integer numerical values. 
The user, in addition, must specify the operation with the first character of the operation that he/she wishes 
to to perform:  ‘S' o ‘s’ for the sum, ‘R’ o ‘r’ for the substaction, ‘M’ o ‘m’ for multiplication and ‘D’ 
o ‘d’ para la division. """
""" switch donot exist"""

menu = str(input("Menu operations: \n (s)um \n (r)substraction \n (m)ultiplication \n (d)ivision "))

if menu == "s" or menu == "S":
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    reply = num1 + num2
    print(reply)

elif menu == "r" or menu == "R":
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    reply = num1 - num2
    print(reply)

elif menu == "m" or menu == "M":
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    reply = num1 * num2
    print(reply)

elif menu == "d" or menu == "D":
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    reply = num1 / num2
    print(reply)

else:
    print("This option does not exist, enter another option")
    menu = str(input("Menu operations: \n (s)um \n (r)substraction \n (m)ultiplication \n (d)ivision "))