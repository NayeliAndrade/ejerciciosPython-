""" Realizar un programa que rellene un vector de tamaño N, con valores ingresados por el
usuario. A continuación, se deberá crear una función que reciba el vector y devuelva el valor
más grande del vector. """

vector = []
tamanoVector = int(input("Ingresa el tamaño del vector: "))

for i in range(0,tamanoVector):
    valores = int(input("Ingresa los valores para el vector: "))
    vector.append(valores)

def mayor(vector,tamanoVector):
    numMayor = 0
    for i in range(0,tamanoVector):
        if vector[i] > numMayor:
            numMayor = vector[i]
    print(numMayor)

mayor(vector,tamanoVector)