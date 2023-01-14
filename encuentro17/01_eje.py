tablero = []

def inicializarMatriz(tablero,fila,columna):
	for i in range(fila):
		tablero.append([])
		for j in range(columna):
			tablero[i].append("*")

def imprimir(tablero):
	for i in tablero:
		print(i,end=" ")
		print("")

def agregarPalabra(tablero, palabra, fila):
	for i in range(len(palabra)):
		tablero[fila][i].append(palabra[i])

inicializarMatriz(tablero,9,12)
imprimir(tablero)
agregarPalabra(tablero, "vector", 0)

""" 
inicializarMatriz(tablero, 9, 12)
agregarPalabra(tablero, "vector", 0)
agregarPalabra(tablero, "matrix", 1)
agregarPalabra(tablero, "programa", 2)
agregarPalabra(tablero, "subprograma", 3)
agregarPalabra(tablero, "subproceso", 4)
agregarPalabra(tablero, "variable", 5)
agregarPalabra(tablero, "entero", 6)
agregarPalabra(tablero, "para", 7)
agregarPalabra(tablero, "mientras", 8)
acomodarPalabras(tablero)
imprimirMatriz(tablero, 9, 12)
FinAlgoritmo
 """