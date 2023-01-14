""" Realizar una función que permita obtener el término n de la sucesión de Fibonacci. La sucesión de Fibonacci es
 la sucesión de los siguientes números:
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Donde cada uno de los números se calcula sumando los dos anteriores a él. Por ejemplo:
La sucesión del número 2 se calcula sumando (1+1)
Análogamente, la sucesión del número 3 es (1+2),
Y la del 5 es (2+3),
Y así sucesivamente…
La sucesión de Fibonacci se puede formalizar de acuerdo a la siguiente fórmula:
Fibonacci (n) = Fibonacci (n-1) + Fibonacci (n-2) para todo n > 1
Fibonacci (n) = 1 para todo n <= 1
Por lo tanto, si queremos calcular el término “n” debemos escribir una función que reciba como argumento el valor 
de “n” y que calcule la serie hasta llegar a ese valor.
Para conocer más acerca de la serie de Fibonacci consultar el siguiente link:
 https://quantdare.com/numeros-de-fibonacci/ """

number = int(input("Enter a number: "))

def fibonacci(number):
    n1 =0
    n2 =1
    for i in range(1,number):
        sum=n1+n2
        n1=n2
        n2=sum
        print(sum)

fibonacci(number)