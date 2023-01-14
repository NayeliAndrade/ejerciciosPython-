"""Program a game where the computer chooses a random number between 1 and 10, and then the player has to guess it. 
has to guess it. The program structure is as follows:
1st) The program randomly chooses a number n between 1 and 10.
2º) The user enters a number x.
3º) If x is not the exact number, the program indicates whether n is larger or smaller than the number entered.
4º) We repeat from 2) until x is equal to n.
The program has to print the appropriate messages to tell the user what to do and what happened until he/she 
guess the number."""

import random 

numRandom = random.randint(1,10)
""" print(numRandom) """

numUser = int(input("Enter a number between 1 and 10: "))

while numUser != numRandom:
    if numUser != numRandom:
    
        if numRandom < numUser:
            print("number is lower")
            numUser = int(input("Enter a number: "))
        else:
            print("Number is greater")
            numUser = int(input("Enter a number: "))
    else:
        print("This is the number")

if numUser == numRandom:
    print("This is the number")
