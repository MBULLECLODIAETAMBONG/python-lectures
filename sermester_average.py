#                      EXERCISE
# It's the end of the semester and you got your marks from, Geometry, Algebra and Physics classes. If the average score is 7
# and above print "c", if the average score is between 6 and 4 print "You need to work harder!", 
# if the average score is below 4 print "Failed, you really need to work harder!".

#                         SOLUTION

#             METHOD 1

Geometry = float(input("Enter the marks scored for Geometry: "))
Algebra = float(input("Enter the marks scored for Algebra : "))
Physics = float(input("Enter the marks scored for Physics: "))
print("Geometry: ",Geometry,"\n Algebra: ",Algebra, "\n Physics: ",Physics)

total_scored = (Geometry + Algebra + Physics) 
average_marks = (total_scored / 30) * 100 

if average_marks >= 70:
    print("Good Job!")
elif(average_marks >=40 and average_marks <=60 ):
    print("You Need to work hard!")
else:
    print("Failed, you really need to work harder!")

#       METHOD 2 Using a function
 
def average_score(Geometry, Algebra, Physics):
    total_scored = (Geometry + Algebra + Physics) 
    average_marks = (total_scored / 3) * 100 

    if average_marks >= 70:
        print("Good Job!")
    elif(average_marks >=40 and average_marks <=60 ):
        print("You Need to work hard!")
    else:
        print("Failed, you really need to work harder!")
        
get_course_marks = average_score(float(input("Enter the marks scored for Geometry: ")),
 float(input("Enter the marks scored for Algebra : ")),
float(input("Enter the marks scored for Physics: "))
)

get_course_marks


