""" Realizar un programa que cree una matriz de 5x15 y deberemos llenar la matriz de unos y
ceros. Llenando el marco o la delimitación externa de la matriz de unos y la parte interna de
ceros.
Por ejemplo, nuestro matriz final debería verse así:
111111111111111
100000000000001
100000000000001
100000000000001
111111111111111 """

matriz = []

for i in range(5):
    matriz.append([])
    for j in range(15):
        if i == 0 or i == 4: 
            matriz[i].append(1)
        elif j == 0 or j == 14:
            matriz[i].append(1)
        else:
            matriz[i].append(0)

for i in matriz:
    print(i,end=" ")
    print(" ")