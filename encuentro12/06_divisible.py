""" Realizar una función que calcule y retorne la suma de todos los divisores del número n distintos de n.
 El valor de n debe ser ingresado por el usuario. """

num = int(input("Enter a number: "))

def suma(num):
    divisores = [1]
    suma=0
    for i in range(2,num+1):
        if num % i == 0:
            divisores.append(i)
    print(divisores)
    for j in divisores:
        suma+=j
    print(suma)
    
suma(num)