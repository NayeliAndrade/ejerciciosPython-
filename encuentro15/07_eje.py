""" Crear un subproceso que rellene dos arreglos de tamaño n, con números aleatorios. Después,
hacer una función que reciba los dos arreglos y diga si todos sus valores son iguales o no. La
función debe devolver el resultado de está validación, para mostrar el mensaje en el
algoritmo. """

import random

vectorA = []
vectorB = []

tamanoVector = int(input("Ingresa el tamaño del vector: "))

def llenarVectorA(tamanoVector):
    for i in range(0,tamanoVector):
        numAleatorio = random.randint(1,15)
        vectorA.append(numAleatorio)
    print(vectorA)

def llenarVectorB(tamanoVector):
    for i in range(0,tamanoVector):
        numAleatorio = random.randint(1,15)
        vectorB.append(numAleatorio)
    print(vectorB)

def comparacion(tamanoVector):
    for i in range(0,tamanoVector):
        if vectorA[i] == vectorB[i]:
            print("El numero en la posicion ", i," Son iguales")
        else:
            print("El numero en la posicion ", i,"Son diferentes")

llenarVectorA(tamanoVector)
llenarVectorB(tamanoVector)
comparacion(tamanoVector)