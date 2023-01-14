""" Teniendo en cuenta que la clave es “eureka”, escribir un programa que nos pida ingresar
 una clave. Sólo se cuenta con 3 intentos para acertar, si fallamos los 3 intentos se deberá 
 mostrar un mensaje indicándonos que hemos agotado esos 3 intentos. Si acertamos la clave se 
 deberá mostrar un mensaje que indique que se ha ingresado al sistema correctamente. """

contador = 0
contrasena = 'eureka'
entrada = str(input('Ingrese la contraseña: '))
esContrasenaCorrecta = False

while not esContrasenaCorrecta: # no es verdadera
    if entrada == contrasena:
        esContrasenaCorrecta = True
        print('Bienvenido')
    else:
        print('Contraseña incorrecta, intente de nuevo')
        contador += 1
        if contador == 3:
            print('Contraseña incorrecta, se ha bloqueado el sistema')
            break
        entrada = str(input('Ingrese la contraseña: '))

    