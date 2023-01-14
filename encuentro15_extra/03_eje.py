""" crear 2 vectores con el mismo tamaño, el usuario ingresa un nombre en uno de los vectores y en el otro 
la longitud del nombre """

vectorA = []
vectorB = []

tamanoVector = int(input("Ingresa el tamaño del vector: "))

def nombres(tamanoVector):
    for i in range(0,tamanoVector):
        nombre = str(input("Ingresa el nombre: "))
        vectorA.append(nombre)
    print(vectorA)

def longitudNombre(tamanoVector):
    for i in range(0,tamanoVector):
        longitud = len(vectorA[i])
        vectorB.append(longitud)
    print(vectorB)

nombres(tamanoVector)
longitudNombre(tamanoVector)