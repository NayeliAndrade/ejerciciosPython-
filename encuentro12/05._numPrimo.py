""" Realizar una función que reciba un numero ingresado por el usuario y averigüe si el número es primo o no.
 Un número es primo cuando es divisible sólo por 1 y por sí mismo, por ejemplo: 2, 3, 5, 7, 11, 13, 17, etc. 
 Nota: recordar el uso del %. """


num = int(input("Enter a number: "))

def primo(num):
    if num > 1:
        counter=0
        i = 2
        while i < num and counter ==0:
            rest=num%i
            if rest==0:
                counter+=1
            i+=1
        if counter ==0:
            print("The number is primo")
        else:
            print("the number is not primo")
    else: 
        print("number is not primo")
    
primo(num)