#4
"""Write a program that calculates how many liters of fuel a car consumed.
The user will enter a number of liters of fuel loaded at the station and a number of kilometers driven. 
number of kilometers traveled, then the program will calculate the consumption (km/lt) and show it to the user.
and display it to the user  """

liters = float(input("How many liters?: "))
kilometers = float(input("kilometers"))

fuel = float(kilometers / liters)
print(fuel)