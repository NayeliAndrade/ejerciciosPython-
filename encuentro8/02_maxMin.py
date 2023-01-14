"""Write a program that reads integers up to 0 (zero). At the end of the program you should 
show the maximum number entered, the minimum, and the average of all of them. In order to achieve, for example, 
the maximum we will initialize a variable in zero called numberMaximum. Then we will compare each number entered
with this variable. is entered with this variable. If it is greater we will replace the value of numberMaximum. 
For example if 5>0 then the maximum between these numbers will be 5. If I then enter the number 2, it evaluates 
to 2>5 which will be false and therefore the value of numberMaximum will be 5. 
therefore the value 5 of numberMaximum is not replaced. A similar logic will have the smaller number.  """

sum = 0
counter = 0
num = int(input("Enter a number: "))
numberMaximum = num
numberMinumun = num
while num != 0:
    if num != 0: 
        sum = sum + num
        counter+=1
        num = int(input("Enter a number: "))
        if  num > numberMaximum:
            numberMaximum = num
        if num < numberMinumun:
            numberMinumun = numberMinumun
           
    if num == 0:
        print("Number maximun: ",numberMaximum)
        print("Number minimun: ",numberMinumun)
        average = sum / counter
        print("average: ",average)