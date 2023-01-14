""" Realizar una función que reciba un numero ingresado por el usuario y averigüe si el número es capicúa o no 
(Por ejemplo: 12321). Nota: recordar el uso del MOD(%) y el Trunc(//). No podemos transformar el numero a cadena para 
realizar el ejercicio. """

number = int(input("Enter a number: "))
a = []
b = []

def flipNumber(number):
    while number != 0:
        individualNum = number % 10
        number = number // 10
        #print(individualNum)
        a.append(individualNum)
        b.append(individualNum)
        rev = b[::-1]
    
    if a == rev:
        print("El numero es capicua")
    else:
        print("El numero no es capicua")

    print("a",a)
    print("b",rev)

flipNumber(number)