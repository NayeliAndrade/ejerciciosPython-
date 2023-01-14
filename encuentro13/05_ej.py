""" Crea un procedimiento “convertirEspaciado”, que reciba como argumento un texto y muestra una cadena con 
un espacio adicional tras cada letra.
Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicho 
procedimiento """

sentence = str(input("Enter a sentence: "))

def converteSpace(sentence):
    for i in sentence: 
        print(i,end=" ")

converteSpace(sentence)