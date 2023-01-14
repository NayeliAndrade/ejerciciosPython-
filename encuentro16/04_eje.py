""" Rellenar en un subproceso una matriz cuadrada con números aleatorios salvo en la diagonal
principal, la cual debe rellenarse con ceros. Una vez llena la matriz debe generar otro
subproceso para imprimir la matriz. """

import random
tamano = int(input("Ingresa el tamaño de las filas y columnas: "))
matriz = []

def generar():
    for i in range(tamano):
        matriz.append([])
        for j in range(tamano):
            numero = random.randint(1,10)
            if i == j: 
                matriz[i].append(0)
            else:
                matriz[i].append(numero)

def imprimir():
    for i in matriz:
        print(i,end=" ")
        print(" ")

generar()
imprimir()