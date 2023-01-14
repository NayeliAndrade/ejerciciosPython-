""" 
cambio de vocales por simbolos
a = @
e = #
i = $
o = %
u = * 
Por ejemplo, si el usuario ingresa: Ayer, lunes, salimos a las once y 10.
La salida del programa debería ser: @y#r, l*n#s, s@l$m%s @ l@s %nc# y 10."""

sentence = str(input("Enter a sentence: "))
print(sentence.replace("a","@").replace("e","#").replace("i","$").replace("o","%").replace("u","*"))


""" 
recorrer oracion por cada letra 
for i in sentence:
    if i == "a":
        print(sentence.replace("a","@"))
    if i == "e":
        print(sentence.replace("e","#"))
    if i == "i":
        print(sentence.replace("i","$"))
    if i == "o":
        print(sentence.replace("o","%"))
    if i == "u":
        print(sentence.replace("u","*")) """