""" Realizar una función que calcule la suma de los dígitos de un número.
Ejemplo: 25 = 2 + 5 = 7
Nota: Para obtener el último número de un digito de 2 cifras o más debemos pensar en el resto de una división 
entre 10. Recordar el uso de % y //. """


number = str(input("Enter a number: "))

if len(number) == 2:
    number = int(number)
    def sum(number):
        number1 = number // 10
        number2 = number % 10
        r = number1 + number2
        print(r)
else:
    print("Only 2 digits are added")

sum(number)