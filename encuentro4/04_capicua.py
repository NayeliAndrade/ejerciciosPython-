#4
"""Design an algorithm that reads a three-digit number and determines whether or not it is capicuous."""

n = int(input("Enter a number: "))

if n > 99 and n < 1000:
    a = n // 100
    c = n % 10

    if a == c:
        print("The number ", n," is a number capicuous")
    else:
        print("The number ", n," is not capicuous")

else:
    print("Enter a three-digit number: ")