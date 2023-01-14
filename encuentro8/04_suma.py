""" A program must be made that:
1º) Requests by keyboard a number (positive integer).
2º) Ask the user if he/she wants to enter another number or not.
3º) Repeat steps 1 and 2 as long as the user does not answer n/N (no).
4th) Display the sum of the numbers entered by the user."""

sum = 0
num = 0
ask = "si" 

while ask == "Y" or ask == "y" or ask == "yes" or ask == "YES" or ask == "Yes" or ask == "yeS":
    num = int(input("Enter your number: "))
    ask = str(input("you want to enter another: (Y)es o (N)o "))
    sum = sum + num
    if ask == "N" or ask == "n" or ask == "no" or ask == "NO" or ask == "No" or ask == "nO":
        print("the sum of the numbers is : ",sum)