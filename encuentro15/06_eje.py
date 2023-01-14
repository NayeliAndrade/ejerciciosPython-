""" a) Pida una frase al usuario y luego ingrese la frase dentro del arreglo letra por letra. """
""" b) Una vez completado lo anterior, pedirle al usuario un carácter cualquiera y una
posición dentro del arreglo, y el programa debe intentar ingresar el carácter en la
posición indicada, si es que hay lugar (es decir la posición está vacía o es un espacio
en blanco). De ser posible debe mostrar el vector con la frase y el carácter ingresado,
de lo contrario debe darle un mensaje al usuario de que esa posición estaba ocupada """

vector = []

frase = str(input("Ingresa una frase: "))

""" vector.append(frase) """

""" cantidadLetras = (len(frase))
print(cantidadLetras) """

def dividePalabra(vector,frase):
    for i in range(len(frase)):
        vector.append(frase[i])
        print(frase[i])
        print(vector)

caracter = str(input("Ingresa un caracter: "))
posicion = int(input("Ingresa una posicion que se encuentre dentro del arreglo: "))

def insertarLetra(vector,caracter,posicion):
    for i in range(len(frase)):
        if posicion <= len(frase):
            vector[posicion].append(caracter)
            print(vector)
        else:
            print("La posicion ingresada esta ocupada por la letra: ",vector[i])
            print(vector)

dividePalabra(vector,frase)
insertarLetra(vector,caracter,posicion)