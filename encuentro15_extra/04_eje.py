""" agregar 100 notas de las cuales te digan cuantas son deficientes, buenas,regulares,excelentes """

import random
vectorNotas = []

deficiente = 0
bueno = 0
regular = 0
excelente = 0

for i in range(0,100):
    nota = random.randint(0,20)
    vectorNotas.append(nota)
    
    if vectorNotas[i] >= 0 and vectorNotas[i] <=5:
        deficiente += 1
    elif vectorNotas[i] >= 6 and vectorNotas[i] <= 10:
        regular += 1
    elif vectorNotas[i] >= 11 and vectorNotas[i] <= 15:
        bueno +=1
    elif vectorNotas[i] >= 16 and vectorNotas[i] <= 20:
        excelente +=1

print(vectorNotas)
print("En Deficientes hay: ", deficiente, "notas")
print("En Regular hay: ", regular, "notas")
print("En Bueno hay: ", bueno, "notas")
print("En Excelente hay: ", excelente, "notas")