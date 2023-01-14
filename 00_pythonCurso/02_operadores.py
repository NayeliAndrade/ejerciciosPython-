#operadores aritmeticos 

#operadores con enteros 
print(3+2)
print(7-4)
print(3*4)
print(10*2)
print(2**2)
print(2 ** 3 + 3 - 7 / 1 // 4)

#operaciones con cadenas de texto
print('hola ' + 'python ' + 'que')
print('hola ' + str(4))

#operaciones mixtas
print('hola ' * 5)
print('hola ' * (2**3))

my_float = 2.5 * 2
print('hola ' * int(my_float))

#operadores comparativos 
#operadores con enteros
print(3 > 4)
print(3 < 5)
print(3 >= 5)
print(4 <= 5)
print(3 == 3)
print(3 != 4)

#operadores con cadena de texto
print('hola' > 'python')
print('hola' < 'python')
print("aaaa" >= "abaa") # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))