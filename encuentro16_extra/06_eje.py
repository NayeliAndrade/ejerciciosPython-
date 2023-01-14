""" Realizar un programa que permita visualizar el resultado del producto de una matriz de
enteros de 3x3 por un vector de 3 elementos. Los valores de la matriz y el vector pueden
inicializarse evitando así el ingreso de datos por teclado. Para conocer más acerca de cómo se
realiza la multiplicación entre matrices consultar el siguiente link:
https://es.wikibooks.org/wiki/%C3%81lgebra_Lineal/Matriz_por_vector """

import random

matrizA = []
vector = []
aux = []

for i in range(3):
    numero = random.randint(1,9)
    vector.append(numero)
    matrizA.append([])
    for j in range(3):
        numero2 = random.randint(1,9)
        matrizA[i].append(numero2)

for i in matrizA:
    print(i,end=" ")
    print(" ")
print(" ")

for i in vector:
    print(i,end="")
    print("")


for i in range(3):
    aux.append([])
    aux[i] = 0
    for j in range(3):
        aux[i] = (vector[i]*matrizA[i][j]) + aux[i]
print(" ")

for i in aux:
    print(i,end=" ")
    print(" ")
