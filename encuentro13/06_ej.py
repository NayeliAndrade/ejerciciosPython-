""" Realizar una funcion que reciba una letra y muestre un mensaje si esa letra esta entre las letras
 “M” y “T”. """

letter = str(input("Enter a sentence: ").upper())

def findLetter(letter):
    if len(letter) == 1:
        if letter == "N":
            print("True")
        elif letter == "Ñ":
            print("True")
        elif letter == "O":
            print("True")
        elif letter == "P":
            print("True")
        elif letter == "Q":
            print("True")
        elif letter == "R":
            print("True")
        elif letter == "S":
            print("True")
        elif letter == "T":
            print("True")
        else:
            print("The letter is not find")
    else:
        print("Just enter one letter")
    
findLetter(letter)

