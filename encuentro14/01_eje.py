def calcularMuro():
    muro = int(input("El muro es de 20 o 30 cm de espesor? "))
    largo = float(input("Ingresa el largo: "))
    alto = float(input("Ingresa el alto: "))

    superficieMuro = largo * alto
    print("La superficie del nuro es de: ",superficieMuro, "m2")

    if muro == 20:
        cemento = 10.9 * superficieMuro 
        arena = 0.09 * superficieMuro
        ladrillos = 90 * superficieMuro
        print("Necesitamos por metro cuadrado: ", cemento, "cemento", " kg de cemento, ",arena," m3 de arena y ",ladrillos," ladrillos")
    elif muro == 30:
        cemento = 15.2 * superficieMuro
        arena = 0.115 * superficieMuro
        ladrillos = 120 *superficieMuro
        print("Necesitaremos por metro cuadrado: ",cemento, " kg de cemento, ",arena," m3 de arena y ",ladrillos," ladrillos.")
    else:
        print("Ingresa una cantidad valida de espesor")

def calcularViga():
    largoViga = float(input("Ingrese el largo de la viga: ")) 

    cemento = 9* largoViga
    arena = 0.02 * largoViga
    piedra = 0.02 * largoViga
    hierro4 = 3 * largoViga
    hierro8 = 4* largoViga

    print("Por metro lineal de viga se necesitarán: ",cemento," kg de cemento, ",arena," m3 de arena, ",piedra," m2 de piedra, ",hierro8," m de hierro del 8 y ",hierro4," m de hierro del 4.")
	
def calcularColumna():
    largoColumna = float(input("Ingrese el largo de la columna: ")) 

    cemento = 7.5 * largoColumna
    arena = 0.016 * largoColumna
    piedra =  0.016 * largoColumna
    hierro10 = 6 * largoColumna
    hierro4 = 3 * largoColumna

    print("se necesitarán: ",cemento," kg de cemento, " ,arena,"  m3 de arena,",piedra," m2 de piedra, ",hierro10," m de hierro del 10 y ",hierro4," m de hierro del 4.")

def calcularContrapisos():
	espesorContrapiso = float(input("Ingrese el espesor del contrapiso: ")) 
	ancho = float(input("Ingrese el ancho del contrapiso: ")) 
	largo = float(input("Ingrese el largo del contrapiso: ")) 
	
	rcontra = espesorContrapiso * ancho * largo
	cemento = 105* rcontra
	arena = 0.45* rcontra
	piedra = 0.9* rcontra

	print("se necesita: ",cemento," kg de cemento, ",arena," m3 de arena y ",piedra," m3 de piedra.")

def calcularTecho():
    espesor = float(input("Ingrese el espesor del contrapiso: ")) 
    ancho = float(input("Ingrese el ancho del contrapiso: ")) 
    largo = float(input("Ingrese el largo del contrapiso: ")) 
    
    rtecho = espesor * ancho * largo
    cemento= 33* rtecho
    arena= 0.072* rtecho
    piedra= 0.072* rtecho
    hierro8=7 * rtecho
    hierro6= 4 * rtecho
    
    print("se necesita: ",cemento," kg de cemento, ",arena," m3 de arena, ",piedra," m3 de piedra, ",hierro8," m de hierro del 8 y ",hierro6," m de hierro del 6")

def calcularPiso():
    ancho = float(input("Ingrese el ancho del piso: ")) 
    largo = float(input("Ingrese el largo del piso: ")) 
	
    r1 = (ancho* largo) / 0.90
    print("El total del piso es: ", r1 ," m2")

def calcularPintura():
	
	litrosPintura = float(input("Ingrese la superficie del muro: ")) 
	
	litrosPintura = litrosPintura * 6	
	print("Necesitamos ",litrosPintura," litros de pintura")
	
def calcularIluminacion():
	superficie = float(input("Ingrese la superficie: ")) 

	iluminacion = superficie * 0.20
	print("la cantidad mínima de superficie de iluminación natural (ventanas y puertas de vidrio) es: ", iluminacion)
	

menu = int(input("Ingresa el numero de la opcion que mas te guste: \n 1.calcular muro de ladrillos \n 2.calcular viga de hosuperficieMuroigon \n 3.Calcular columnas de hormigón \n 4.Calcular contrapisos \n 5.Calcular techo \n 6.Calcular pisos \n 7.Calcular pintura \n 8.Calcular iluminación \n 9.Salir "))

if menu == 1:
    print("1")
    calcularMuro()
elif menu == 2:
    print("2")
    calcularViga()
elif menu == 3:
    print("3")
    calcularColumna()
elif menu == 4:
    print("4")
    calcularContrapisos()
elif menu == 5:
    print("5")
    calcularTecho()
elif menu == 6:
    print("6")
    calcularPiso()
elif menu == 7:
    print("7")
    calcularPintura()
elif menu == 8:
    print("8")
    calcularIluminacion()
elif menu == 9:
    print("9")
    print("salir")
else:
    print("Error, ingresa respuesta valida")