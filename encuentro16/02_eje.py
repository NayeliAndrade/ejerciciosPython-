""" Escribir un programa que realice la búsqueda lineal de un número entero ingresado por el
usuario en una matriz de 5x5, llena de números aleatorios y devuelva por pantalla las
coordenadas donde se encuentra el valor, es decir en que fila y columna se encuentra. En
caso de no encontrar el valor dentro de la matriz se debe mostrar un mensaje """

import random
matriz = []

for i in range(5):
    matriz.append([])
    for j in range(5):
        numero = random.randint(1,10)
        matriz[i].append(numero)
        
for i in matriz:
    print(i,end=" ")
    print(" ")

buscar = int(input("Ingresa el numero que quieres buscar: "))

for i in range(5):
    for j in range(5):
        if buscar == matriz[i][j]:
            print(f"numero fila {i}, numero columna {j}")
        else:
            print("No se encuentra ese numero")