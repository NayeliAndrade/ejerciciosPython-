"""Realizar un programa que rellene 2 vectoores al mismo tiempo, con 5 valores aleatorios y los muestra 
por pantalla"""

import random

vectorA = []
vectorB = []

def llenarVectorA():
    for i in range(0,5):
        numAleatorio = random.randint(1,15)
        vectorA.append(numAleatorio)
    print(vectorA, "Vector A")

def llenarVectorB():
    for i in range(0,5):
        numAleatorio = random.randint(1,15)
        vectorB.append(numAleatorio)
    print(vectorB, "Vector B")

llenarVectorA()
llenarVectorB()