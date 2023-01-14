""" Realizar una función que calcule la suma de dos números. En el algoritmo principal le pediremos al usuario 
los dos números para pasárselos a la función. Después la función calculará la suma y lo devolverá para imprimirlo 
en el algoritmo. """

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

def sum(num1,num2):
    result = num1 + num2
    print(result)

sum(num1,num2)