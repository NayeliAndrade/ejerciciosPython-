#1
"""A man wants to know if his salary is higher than the minimum wage, the program will ask the user for 
his current salary and the minimum wage. the user for his current salary and the minimum salary. If the 
salary is higher than the minimum wage, a message should be a message should be displayed on the screen 
indicating this.  """

salary = int(input("Enter your salary: "))
minimumSalary = int(input("Enter your minimum salary: "))

if salary > minimumSalary:
    print("Your salary is higher: ")