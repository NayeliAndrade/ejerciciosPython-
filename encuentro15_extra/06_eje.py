""" crea una funcion que debuelva la diferencia que hay entre el valor mas chico de un arreglo y su valor mas grande """

import random
vector = []
tamano = int(input("Ingresa el tamaño del arreglo: "))

def llenarVector(vector):
    for i in range(0,tamano):
        numero = random.randint(1,100)
        vector.append(numero)
    print(vector)
    
def diferencia():
    numMayor = 0
    numMenor = vector[0]
    for j in range(0,tamano):
        

        if vector[j] > numMayor:
            numMayor = vector[j]
            
        if vector[j] <= numMenor:
            numMenor = vector[j]
            
      
    print("Numero mayor es: ",numMayor)
    print("Numero menor es: ",numMenor)

llenarVector(vector)
diferencia()