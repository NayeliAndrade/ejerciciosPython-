""" Realizar un programa que pida al usuario una frase y una letra a buscar en esa frase. La función debe devolver
 la cantidad de veces que encontró la letra. """

frase = str(input("Ingresa una frase: "))
letra = str(input("Ingresa una letra: "))

def cuantasLetras(frase,letra):
    print(frase.count(letra))

cuantasLetras(frase,letra)
