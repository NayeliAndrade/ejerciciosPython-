""" Crear una función llamada “Login”, que recibe un nombre de usuario y una contraseña y que devuelve 
Verdadero si el nombre de usuario es “usuario1” y si la contraseña es “asdasd”. Además, la función calculara
 el número de intentos que se ha usado para loguearse, tenemos solo 3 intentos, si nos quedamos sin intentos 
 la función devolverá Falso. """

user = str(input("Enter your user: "))
password = str(input("Enter a password: "))

def login(user,password):
    counter = 1
    if user == "usuario1" and password == "asdasd":
        print("True")
    else:
        while counter<3:
            counter+=1
            print("false")
            user = str(input("Enter your user: "))
            password = str(input("Enter a password: "))
            if user == "usuario1" and password == "asdasd":
                print("true")
                break

login(user,password)