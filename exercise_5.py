# You are developing a program for a teacher to grade their students' exams. 
# The program should prompt the teacher to enter the number of questions on the exam, the number of questions the student answered correctly, and the number of points each question is worth. 
# The program should then calculate the student's grade as a percentage, and print out a message indicating whether the student passed or failed the exam.

# prompting the teacher to enter the number of questions on the exam
number_of_questions = int(input("Enter the number of questions: "))

# prompting the teacher to enter the number of questions the student answered correctly
number_of_questions_answered_correctly = int(input("Enter the number of questions student answered correctly: "))

# prompting the teacher to enter the number of points each question is worth
number_of_points_each_worth = int(input("Enter the points each question is worth: "))

# calculating the total number of points the student scored
total_number_of_points = (number_of_questions_answered_correctly * number_of_points_each_worth)

# Calculating the maximum points for the exam 
maximum_number_of_points = (number_of_questions * number_of_points_each_worth)

# calculating the student's grade as a percentage
student_grade = (total_number_of_points / maximum_number_of_points) * 100

# checking is the student fails or not
if(student_grade >= 50):
    print("The student passed the exam with:", student_grade, "%") 
else:
    print("The student failed the exam with: ", student_grade, "%")


