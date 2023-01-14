#2
"""Construct a pseudocode that allows to enter a number, if the number is greater than 500, 
18% of this number must be calculated and displayed on the screen.  """

num = int(input("Enter your number: "))

if num > 500:
    calculated = num * 0.18
    print("el porcentaje es: ",calculated)