""" Diseñar una función que reciba un numero en forma de cadena y lo devuelva como numero entero. El 
programa podrá recibir números de hasta 3 dígitos. Nota: no poner números con decimales ni letras. Ejemplo: 
ingresando “100”(carácter) debe convertirse en 100(entero). """

num = str(input("Enter a number of 3 digits: "))

if len(num) == 3:
    converted = int(num)
    print(type(converted))
    print("number integer: ",converted)
else:
    print("This number contains more than 3 digits")


