""" programe una funcion donde optengas el producto de los numeros que se encuentran adentro del vector """

import random
vector = []
tamano = int(input("Ingresa el tamaño del arreglo: "))

def agregar(vector):
    for i in range(0,tamano):
        numero = random.randint(1,10)
        vector.append(numero)
    print(vector)

def multiplicacion(vector):
    producto = 1
    for i in vector:
        producto *= i
    print(producto)

agregar(vector)
multiplicacion(vector)