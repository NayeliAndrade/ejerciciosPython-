""" Realizar un programa con el siguiente menú y le pregunte al usuario que quiere hacer hasta
que ingrese la opción Salir:
A. Llenar Vector A. Este vector es de tamaño N y se debe llenar de manera aleatoria
usando la función Aleatorio(valorMin, valorMax) de PseInt.
B. Llenar Vector B. Este vector también es de tamaño N y se llena de manera aleatoria.
C. Llenar Vector C con la suma de los vectores A y B. La suma se debe realizar elemento
a elemento. Ejemplo: C = A + B
D. Llenar Vector C con la resta de los vectores B y A. La resta se debe realizar elemento a
elemento. Ejemplo: C = B - A
E. Mostrar. Esta opción debe permitir al usuario decidir qué vector quiere mostrar: Vector
A, B, o C.
F. Salir. """

import random

vectorA = []
vectorB = []
vectorCSuma = []
vectorCResta = []

menu = int(input("Ingresa la opcion del menu que mas te guste: \n (1).Llenar vetor A \n (2).Llenar vector B \n (3).Suma vectores \n (4).Resta vectores \n (5).Mostrar \n (0).Salir "))
tamanoVector = int(input("Ingresa el tamaño del vector: "))

def llenarVectorA(tamanoVector):
    for i in range(tamanoVector):
        numAleatorio = random.randint(1,15)
        vectorA.append(numAleatorio)
    print(vectorA)
        
def llenarVectorB(tamanoVector):
    for i in range(0,tamanoVector):
        numAleatorio = random.randint(1,15)
        vectorB.append(numAleatorio)
    print(vectorB)

def llenarVectorCSuma(tamanoVector):
    llenarVectorA(tamanoVector)
    llenarVectorB(tamanoVector)
    for i in range(0,tamanoVector):
        suma = vectorA[i] + vectorB[i]
        vectorCSuma.append(suma)
    print(vectorCSuma)

def llenarVectorCResta(tamanoVector):
    llenarVectorA(tamanoVector)
    llenarVectorB(tamanoVector)
    for i in range(0,tamanoVector):
        resta = vectorB[i] - vectorA[i]
        vectorCResta.append(resta)
    print(vectorCResta)

while menu != 0:
    if menu == 1:
        llenarVectorA(tamanoVector)
        menu = int(input("Ingresa la opcion del menu que mas te guste: \n (1).Llenar vetor A \n (2).Llenar vector B \n (3).Suma vectores \n (4).Resta vectores \n (5).Mostrar \n (0).Salir "))
    elif menu == 2:
        llenarVectorB(tamanoVector)
        menu = int(input("Ingresa la opcion del menu que mas te guste: \n (1).Llenar vetor A \n (2).Llenar vector B \n (3).Suma vectores \n (4).Resta vectores \n (5).Mostrar \n (0).Salir "))
    elif menu == 3:
        llenarVectorCSuma(tamanoVector)
        menu = int(input("Ingresa la opcion del menu que mas te guste: \n (1).Llenar vetor A \n (2).Llenar vector B \n (3).Suma vectores \n (4).Resta vectores \n (5).Mostrar \n (0).Salir "))
    elif menu == 4:
        llenarVectorCResta(tamanoVector)
        menu = int(input("Ingresa la opcion del menu que mas te guste: \n (1).Llenar vetor A \n (2).Llenar vector B \n (3).Suma vectores \n (4).Resta vectores \n (5).Mostrar \n (0).Salir "))
    elif menu == 5:
        opcion = int(input("Quieres imprimir \n1.Vector A \n2.Vector B \n3.Vector c suma \n4.Vector c resta"))
        if opcion == 1:
            llenarVectorA(tamanoVector)
            print(vectorA)
            menu = int(input("Ingresa la opcion del menu que mas te guste: \n (1).Llenar vetor A \n (2).Llenar vector B \n (3).Suma vectores \n (4).Resta vectores \n (5).Mostrar \n (0).Salir "))
        elif opcion == 2:
            llenarVectorB(tamanoVector)
            print(vectorB)
            menu = int(input("Ingresa la opcion del menu que mas te guste: \n (1).Llenar vetor A \n (2).Llenar vector B \n (3).Suma vectores \n (4).Resta vectores \n (5).Mostrar \n (0).Salir "))
        elif opcion == 3:
            llenarVectorCSuma(tamanoVector)
            print(vectorCSuma)
            menu = int(input("Ingresa la opcion del menu que mas te guste: \n (1).Llenar vetor A \n (2).Llenar vector B \n (3).Suma vectores \n (4).Resta vectores \n (5).Mostrar \n (0).Salir "))
        elif opcion == 4:
            llenarVectorCResta(tamanoVector)
            print(vectorCResta)
            menu = int(input("Ingresa la opcion del menu que mas te guste: \n (1).Llenar vetor A \n (2).Llenar vector B \n (3).Suma vectores \n (4).Resta vectores \n (5).Mostrar \n (0).Salir "))
        else:
            print("Esa opcion no existe")
    elif menu == 0:
        print("Salir")      
    else:
        print("No existe esa opcion") 