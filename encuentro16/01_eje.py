""" Realizar un programa que rellene una matriz de 3x3 con 9 valores ingresados por el usuario y
los muestre por pantalla """

matriz = []

for i in range(3):
    matriz.append([])
    for j in range(3):
        numero = int(input("Ingresa numero: "))
        matriz[i].append(numero)

for i in matriz:
    print(i,end=" ")
    print(" ")