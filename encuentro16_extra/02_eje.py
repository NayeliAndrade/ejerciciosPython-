""" matriz transpuesta """
import random
fila = int(input("Tamaño fila: "))
columna = int(input("Tamaño columna: "))

matriz = []
matrizTranspuesta = []

def llenarMatrices(fila,columna,matriz):
    for i in range(0,fila):
        matriz.append([])
        for j in range(0,columna):
            numero = random.randint(1,100)
            matriz[i].append(numero)
            
def imprimirMatriz(matriz):
    for i in matriz:
        print(i,end=" ")
        print(" ")
    print(" ")

def matrizTrans(fila,matriz,matrizTranspuesta):
    for i in range(0,fila):
        matrizTranspuesta.append([])
        for j in range(0,fila):
            matrizTranspuesta[i].append(matriz[j][i])

def imprimirTranspuesta(matrizTranspuesta):
    for i in matrizTranspuesta:
        print(i,end=" ")
        print(" ")

llenarMatrices(fila,columna,matriz)
imprimirMatriz(matriz)
matrizTrans(fila,matriz,matrizTranspuesta)
imprimirTranspuesta(matrizTranspuesta)
