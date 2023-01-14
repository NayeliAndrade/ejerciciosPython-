""" Diseñar un procedimiento que reciba una frase, y el programa remueva todas las vocales repetidas. Al 
final el procedimiento mostrará la frase final.
Por ejemplo:
Entrada: “Habia una vez un barco”
Salida: “Habi un vez n brco"
Se marcan en rojo las repetidas sólo para explicar la consigna. Las vocales ‘e’, ‘i’ y ‘o’ quedan al no estar 
repetidas. """

sentenceUser = str(input("Enter a sentence: "))
contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0

def vocalRepetida(sentenceUser):
    vowels = ["a","e","i","o","u"]
    while vowels in sentenceUser:
        text2 = sentenceUser.replace(vowels," ")
        print(text2)
    """ for i in range(len(sentenceUser)):
        print(sentenceUser[i])
        if sentenceUser[i] == "a":
            sentenceUser[i].replace("a","-") """
vocalRepetida(sentenceUser)





""" a = "hola buenas"

b = list(sentenceUser)
for i in b:
    if i == "a":
        b.replace("a","-")

print(a)
print(b) """




