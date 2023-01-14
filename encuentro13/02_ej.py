""" Crear un procedimiento que calcule la temperatura media de un día a partir de la temperatura máxima 
y mínima. Crear un programa principal, que, utilizando un procedimiento, vaya pidiendo la temperatura 
máxima y mínima de n días y vaya mostrando la media de cada día. El programa pedirá el número de días
 que se van a introducir """

day = int(input("Enter a number of days: "))

def temperature(day):
	for i in range(1,day+1):
		temMax = float(input("Enter the temperature maximum: "))
		temMin = float(input("Enter a temperature minimum: "))
		temMed = (temMax + temMin) / 2
		print("The temperature mean is: ",temMed)
		print(" ")

temperature(day)
