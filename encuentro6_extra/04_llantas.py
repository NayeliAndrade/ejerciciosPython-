"""If less than five tires are purchased the price is $3000 each, if between 5 and 10 the price is $2500,
and if more than 10 are purchased the price is $2000. 5 to 10 the price is $2500, and if more than 10 are 
purchased the price is $2000. Obtain the amount the amount of money a person has to pay for each of the 
tires he buys, and the total amount he has to pay for the total number of tires.he/she has to pay for the 
total purchase """

numberTires = int(input("how many tires did you buy?: "))

if numberTires < 5: 
    print("the price is 3000 each, the total price is: ", numberTires * 3000)
elif numberTires >= 5 and numberTires < 10:
    print("the price is 2500 each, the total price is: ", numberTires * 2500)
elif numberTires >= 10: 
    print("the price is 2000 each, the total price is: ",numberTires * 2000)
else:
    print("error")