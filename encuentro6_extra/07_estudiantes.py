"""The average of the practical work of a course is calculated on the basis of four grades of which the 
lowest grade is eliminated and the three highest grades are averaged. 
of which the lowest grade is eliminated and the three highest grades are averaged. Write a program 
that determines what is the eliminated grade and the average of a student's practical work.  """

rating1 = int(input("enter your rating: "))
rating2 = int(input("enter your rating: "))
rating3 = int(input("enter your rating: "))
rating4 = int(input("enter your rating: "))

if rating1 <= rating2 and rating1 <= rating3 and rating1 <= rating4:
    print("case 1") 
    average= (rating2+rating3+rating4)/3
    print(average)
elif rating2 <= rating1 and rating2 <= rating3 and rating2 <= rating4:
    print("case 2")
    average= (rating1+rating3+rating4)/3
    print(average)
elif rating3 <= rating1 and rating3 <= rating2 and rating3 <= rating4:
    print("case 3")
    average= (rating1+rating2+rating4)/3
    print(average)
elif rating4 <= rating1 and rating4 <= rating2 and rating4 <= rating3:
    print("case 4")
    average= (rating1+rating2+rating3)/3
    print(average)
else:
    print("FAILURE")