""" Realizar una función que valide si un número es impar o no. Si es impar la función debe devolver un verdadero,
 si no es impar debe devolver falso. """
 
num = int(input("Enter a number: "))

def numberEvenOdd(num):
    if num % 2 == 0:
        print("True")
    else:
        print("False")

numberEvenOdd(num)