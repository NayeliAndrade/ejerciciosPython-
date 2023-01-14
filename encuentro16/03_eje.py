""" Dada una matriz de orden n * m (donde n y m son valores ingresados por el usuario) realizar
un subprograma que llene la matriz de numeros aleatorios. Despues, crearemos otro
subprograma que calcule y muestre la suma de los elementos de la matriz. Mostrar la matriz y
los resultados por pantalla. """

import random
fila = int(input("Ingresa tamaño de la fila: "))
columna = int(input("Ingresa tamaño de la columna: "))
matriz = []
sumas = []

def crearMatriz(fila,columna,matriz):
    for i in range(fila):
        matriz.append([])
        for j in range(columna): 
            numero = random.randint(1,10)
            matriz[i].append(numero)

def imprimir(matriz):
    for i in matriz:
        print(i,end=" ")
        print(" ")

def sumaMatrizFila(fila,columna,matriz):
    for i in range(fila):
        sumaFila = 0
        for j in range(columna):
            sumaFila = sumaFila + matriz[i][j]
        sumas.append(sumaFila)
        #print("fila: ",sumaFila)
        
     
def total(sumas):
    resultado = 0
    for i in sumas:
        resultado = resultado + i 
    print("El total de la suma es: ", resultado)

crearMatriz(fila,columna,matriz)
imprimir(matriz)
sumaMatrizFila(fila,columna,matriz)
#print(sumas)
total(sumas)