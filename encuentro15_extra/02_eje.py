""" realiza un programa que rellene un vector de tamaño N, con valores por el usuario y muestra por pantalla
el promdeio de la suma de todos los valores ingresados """

vector = []
tamanoVector = int(input("Ingresa el tamaño del vector: "))

for i in range(0,tamanoVector):
    valores = int(input("Ingresa los valores para el vector: "))
    vector.append(valores)

def promedioFuncion(vector,tamanoVector):
    suma = 0
    for i in range(0,tamanoVector):
        suma = suma + vector[i]
    promedio = suma / tamanoVector
    print(promedio)

promedioFuncion(vector,tamanoVector)