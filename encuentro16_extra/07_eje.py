""" Una empresa de venta de productos por correo desea realizar una estadística de las ventas
realizadas de cada uno de sus productos a lo largo de una semana. Distribuya luego 5
productos en los 5 días hábiles de la semana. Se desea conocer:
a) Total de ventas por cada día de la semana.
b) Total de ventas de cada producto a lo largo de la semana.
c) El producto más vendido en cada semana.
d) El nombre, el día de la semana y la cantidad del producto más vendido.
El informe final tendrá un formato como el que se muestra a continuación:
 """
import random

matriz = []
vector = []
vactorB = []
vectorC = []

mayor = 0 

for i in range(5):
    matriz.append([])
    for j in range(5):
        numero = random.randint(20,100)
        matriz[i].append(numero)

for i in matriz:
    print(i,end=" ")
    print(" ")

for j in range(5):
    vector[j] = 0
    for i in range(5):
        vector[j] = vector[j] + matriz[i][j]

for i in vector:
    print(i,end=" ")
    print(" ")
    print("Total semana")

for j in range(5):
    posicion = 0
    for i in range(5):
        if i == 0:
            mayor = matriz[i][j]
        elif matriz[i][j] > mayor:
            mayor = matriz[i][j]
            posicion = 1
    """ vectorB[j] = posicion + 1  """