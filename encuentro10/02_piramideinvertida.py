""" Escriba un programa que lea un número entero (altura) y a partir de él cree una escalera invertida de
 asteriscos con esa altura. Por ejemplo, si ingresamos una altura de 5 se deberá mostrar: """

height = int(input("enter the height: "))
i = 0

for i in range(1,height+1):
    for j in range(i,height+1):
        print("* ",end=" ")
    print(" ")