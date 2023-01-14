""" Crear una matriz que contenga 3 columnas y la cantidad filas que decida el usuario. Las dos
primeras columnas contendrán valores enteros ingresados por el usuario y en la 3 columna se
deberá almacenar el resultado de sumar el número de la primera y segunda columna. Mostrar
la matriz de la siguiente forma:
3 + 5 = 8
4 + 3 = 7
1 + 4 = 5
 """
 
matriz = []
filas = int(input("Ingresa cantidad de filas: "))

for i in range(filas):
    matriz.append([])
    for j in range(3):
        numero = int(input("Ingresa los numeros que quieres sumar: "))
        matriz[i].append(numero)
        

for i in matriz:
    print(i,end=" ")
    print(" ")

for i in range(filas):
    print(matriz[i][0])
    print(matriz[i][1])
    #print(matriz[i][2])
    suma = matriz[i][0]+ matriz[i][1]
    matriz[i][2].append(suma)
    print(suma,"s")
    print(i,"i")

for i in range(filas):
    for j in range(2):
        if j == 2:
            print(i,end=" ")
            print(" ")
        else:
            print(i,end=" ")
            print(" ")