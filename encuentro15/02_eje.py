""" Realizar un programa que lea 10 números reales por teclado, los almacene en un arreglo y
muestre por pantalla la suma, resta y multiplicación de todos los números ingresados al
arreglo. """

vector = []

suma = 0
resta = 0
multiplicacion = 1

for i in range(10):
    numeros = int(input("Ingresa numeros para hacer las operaciones: "))
    vector.append(numeros)
    print(vector)
    #print(vector[i])

    suma = suma + vector[i]
    resta = resta - vector[i]
    multiplicacion = multiplicacion * vector[i]

print(suma)    
print(resta)
print(multiplicacion)
