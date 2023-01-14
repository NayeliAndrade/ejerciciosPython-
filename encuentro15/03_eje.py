""" Realizar un programa que rellene un vector de tamaño N, con valores ingresados por el
usuario. A continuación, se debe buscar un elemento dentro del arreglo (el número a buscar
también debe ser ingresado por el usuario). El programa debe indicar la posición donde se
encuentra el valor. En caso que el número se encuentre repetido dentro del arreglo se deben
imprimir todas las posiciones donde se encuentra ese valor.
Finalmente, en caso que el número a buscar no está adentro del arreglo se debe mostrar un
mensaje. """

n = 0
posicion = []
tamano = int(input("Ingresa el tamaño del vector: "))

for i in range(0,tamano):
    print("Numero en la posicion numero: ",i)
    num = int(input("Ingresa los valores del arreglo: "))
    posicion.append(num)
    
    
numBuscar = int(input("Ingresa que numero quieres buscar: "))

for i in range(0,tamano):
    if posicion[i] == numBuscar:
        print("El numero se encuentra en la posicion ", i)
        n +=1
    
if n == 0: 
    print("Este numero no se encuentra en la lista")