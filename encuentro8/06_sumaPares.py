"""You are asked to write a program that calculates the sum of the first N even numbers. That is, if 
we enter the number 5 as the value of N, the algorithm should perform the sum of the following values: 2+4+6+8+10. 
values: 2+4+6+8+10."""

sum = 0
num = 0

n = int(input("Enter the number of numbers to enter: "))

for i in range(1,n+1):
    if num % 2 == 0:
        num = int(input("enter a numbers even: "))
        sum+=num
    else:
        print("This number is not even")
print(sum)