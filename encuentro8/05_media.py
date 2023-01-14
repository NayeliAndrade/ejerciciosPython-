"""Make an algorithm to calculate the average of odd and even numbers, only ten numbers will be entered. """

sum = 0

for i in range(1,11):
    num = int(input("Enter a number: "))    
    sum+=num
    """ print(i)
    print(sum) """ 

print(sum / 10) 