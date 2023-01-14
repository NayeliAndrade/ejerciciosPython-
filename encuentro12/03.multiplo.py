""" Crea una función EsMultiplo que reciba los dos números pasados por el usuario, validando que el primer número
 múltiplo del segundo y devuelva verdadero si el primer número es múltiplo del segundo, sino es múltiplo que 
 devuelva falso. """

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

def isMultiplo(num1,num2):
    if num1 % num2 == 0:
        print("True")
    else:
        print("False")

isMultiplo(num1,num2)
    