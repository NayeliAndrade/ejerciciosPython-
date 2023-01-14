#2
""" Write a program that calculates the average price of a product.
The average price must be calculated from the price of the same product in three different establishments. """

price1 = float(input("price 1 "))
price2 = float(input("price 2 "))
price3 = float(input("price 3 "))

average = (price1 + price2 + price3) / 3
print(average)