""" A greengrocer offers apples at a discount according to the following table:
the price of the apple is 15
2 kilos - 10% off
2+ 15%
5 - 20% 
Determine how much a person who buys apples in this grocery store will pay."""

priceApple = 15

appleSold = float(input("How many kilos of apples did you buy? "))

if appleSold == 2: 
    price = priceApple * appleSold
    discount = price * .10
    total = price - discount 
    print("total payable is :",total)
elif appleSold >= 2 and appleSold <5:
    price = priceApple * appleSold
    discount = price * .15
    total = price - discount 
    print("total payable is :",total)
elif appleSold == 5:
    price = priceApple * appleSold
    discount = price * .20
    total = price - discount 
    print("total payable is :",total)
else:
    total = priceApple * appleSold
    print("total a pagar",total)