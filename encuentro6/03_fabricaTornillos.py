"""Write a program to obtain the degree of efficiency of an operator of a screw factory, 
according to the following two conditions imposed on him for a trial period:
- Produce less than 200 defective screws.
- Produce more than 10000 screws without defects.
- The degree of efficiency is determined as follows:
- If it meets none of the conditions, grade 5.
- If only the first condition is met, grade 6.
- If only the second condition is met, grade 7.
- If both conditions are met, grade 8.  """


defectiveScrews = int(input("how many defective screws were generated? "))
screws = int(input("how many screws were generated? "))


""" if defectiveScrews > 200 and screws < 10000:
    print("grade 5")
else: 
    if defectiveScrews < 200 and screws < 10000:
        print("grade 6")
    else: 
        if defectiveScrews > 200 and screws > 10000:
            print("grade 7")
        else: 
            if defectiveScrews < 200 and screws > 10000:
                print("grade 8")
            else:
                print("error") """

if defectiveScrews > 200 and screws < 10000:
    print("grade 5")
elif defectiveScrews < 200 and screws < 10000:
    print("grade 6")
elif defectiveScrews > 200 and screws > 10000:
    print("grade 7")
elif defectiveScrews < 200 and screws > 10000:
    print("grade 8")
else: 
    print("error")