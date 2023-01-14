"""Make a program that asks the user for his user code (an integer greater than zero) and his numeric 
password (another positive integer). his numerical password (another positive integer). The program should
not allow the user to continue until enter 1024 as the user code and 4567 as the password. The program 
terminates when the correct data is entered.  """

code = int(input("Enter your code: "))
password = int(input("Enter password: "))

if code == 1024 and password == 4567:
    print("Congratulation")
        

while code != 1024 or password != 4567:
    print("Error, Enter correct data")
    code = int(input("Enter your code: "))
    password = int(input("Enter password: "))
    if code == 1024 and password == 4567:
        print("congratulation")
    