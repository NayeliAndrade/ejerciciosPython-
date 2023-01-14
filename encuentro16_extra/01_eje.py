""" Realizar un programa que rellene de números aleatorios una matriz a través de un
subprograma y generar otro subprograma que muestre por pantalla la matriz final. """

import random
matriz = []
tamano = int(input("Ingresar el tamaño del vector: "))

def llenarMatriz(matriz,tamano):
    for i in range(0,tamano):
        matriz.append([])
        for j in range(0,tamano):
            numero = random.randint(0,50)
            matriz[i].append(numero)

def imprimir(matriz):
    for i in matriz:
        print(i,end=" ")
        print(" ")

llenarMatriz(matriz,tamano)
imprimir(matriz)