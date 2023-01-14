""" Realizar una función que reciba un numero ingresado por el usuario y averigüe si el número tiene todos sus
 dígitos impares (ejemplo: 333, 55, etc.). Para esto vamos a tener que separar el numero en partes (si es un 
 numero de más de un digito) y ver si cada número es par o impar. Nota: recordar el uso de la función % y 
 // (). No podemos pasar el numero a cadena para realizar el ejercicio. """

numero = int(input("Ingresa los numeros: "))

def recibir(numero):
    while numero != 0:
        diferente = numero % 10
        numero = numero // 10

        if diferente % 2 == 0:
            print("El numero",diferente,"es par")
        else:
            print("El numero",diferente,"es impar")

print("El numero te lo va a entregar del final al inicio")
recibir(numero)