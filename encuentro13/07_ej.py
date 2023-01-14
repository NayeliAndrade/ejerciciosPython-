""" Crear un programa que dibuje una escalera de números, donde cada línea de números comience en 
uno y termine en el número de la línea. Solicitar la altura de la escalera al usuario al comenzar. 
Ejemplo: si se ingresa el número 3:
1
12
123 """

numberLadder = int(input("Enter a number: "))

def ladder(numberLadder):
    for i in range(1,numberLadder+1):
        print(i)
        for j in range(1,i+1):
            print(j,end=".")

ladder(numberLadder)