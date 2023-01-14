""" Realizar un programa que lea un número entero (tamaño del lado) y a partir de él cree un cuadrado de
 asteriscos de ese tamaño. Los asteriscos sólo se verán en el borde del cuadrado, no en el interior. Por 
 ejemplo, si se ingresa el número 4 se debe mostrar: """

number = int(input("Enter one number: "))

for i in range(1,number+1):
    if i==1 or i==number:
        for j in range(1,number+1): # primer fila
            print("*",end=" ")      
        print(" ") 
    else:
        for j in range(1,number+1):  #laterales
            if j == 1 or j == number:
                print("* ",end="")
            else:
                print(end="  ")
    print(" ")


""" cuadrado """
""" for i in range(1,number+1):
    for j in range(1,number+1):
        print("* ",end=" ")
    print(" ") """