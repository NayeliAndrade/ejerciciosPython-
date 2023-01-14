""" matriz magica """

matriz = []
tamano = int(input("Ingresa el tamaño de la matriz mágica: "))
diagonal = []
sumaFila1 = []
sumas = []

def crear(tamano,matriz):
    numero = 1
    if numero > 0 and numero < 10:     
        for i in range(tamano):
            matriz.append([])
            for j in range(tamano):
                numero = int(input("Ingresa un número entre el 1 y 10: "))
                matriz[i].append(numero)

if tamano > 0 and tamano < 10:
    crear(tamano,matriz)
else:
    tamano = int(input("Ingresa el tamaño de la matriz mágica: "))

def imprimir(matriz):
    for i in matriz:
        print(i,end=" ")
        print(" ")

imprimir(matriz)

def fila(tamano,matriz):
    for i in range(0,tamano):
        sumaFila = 0
        sumaColumna = 0
        sumaDiagonal = 0

        for j in range(0,tamano):
            sumaFila = sumaFila + matriz[i][j]
            
            sumaColumna = sumaColumna + matriz[j][i]
            

            if i == j: 
                sumaDiagonal = matriz[i][j]
                diagonal.append(sumaDiagonal)
            

        sumas.append(sumaFila)
        sumas.append(sumaColumna)
        
        
        print(sumaFila,"fila")
        print(sumaColumna,"colu")
        
        

def sum(diagonal):
    for i in range(0,tamano):
        suma = 0
        for j in range(0,tamano):
            suma = suma + diagonal[j]
        print(diagonal,"diagonal")
        print(suma,"sumadiagonal")
    sumas.append(suma)
    print(sumas,"matriz sumas")
    
fila(tamano,matriz)
sum(diagonal)

def validar(sumas):
    """ print(all(x == sumas[0] for x in sumas)) """
    for i in sumas:
        if i == sumas[0]:
            print("La matriz es magica")
        else:
            print("No es magica")
        
        #print(i)

validar(sumas)

""" validar los numeros del 1 al 9 ingresados por el usuario """
""" solo diga una vez es magica o no magica """