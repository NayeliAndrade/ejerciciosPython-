""" Realizar un programa que calcule la multiplicación de dos matrices de enteros de 3x3.
Inicialice las matrices para evitar el ingreso de datos por teclado. """

import random

matrizA = []
matrizB = []
multiplicacion = []

def llenar(matrizA,matrizB):
    for i in range(3):
        matrizA.append([])
        matrizB.append([])
        for j in range(3):
            numero1 = random.randint(1,9)
            numero2 = random.randint(1,9)
            matrizA[i].append(numero1)
            matrizB[i].append(numero2)

def imprimirA(matrizA):
    for i in matrizA:
        print(i,end=" ")
        print(" ")
    print(" ")

def imprimirB(matrizB):
    for i in matrizB:
        print(i,end=" ")
        print(" ")
    print(" ")

def procedimientoMultiplicacion(matrizA,matrizB,multiplicacion):
    for i in range(3):
        multiplicacion.append([])
        for j in range(3):
            multi = matrizA[i][j] * matrizB[i][j]
            multiplicacion[i].append(multi)

def imprimir(multiplicacion):
    for i in multiplicacion:
        print(i,end=" ")
        print(" ")

llenar(matrizA,matrizB)
imprimirA(matrizA)
imprimirB(matrizB)
procedimientoMultiplicacion(matrizA,matrizB,multiplicacion)
imprimir(multiplicacion)