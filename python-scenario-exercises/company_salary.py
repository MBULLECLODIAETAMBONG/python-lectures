#                           Exercise 1
#In a company the monthly salary of an employee is calculated by: the minimum wage 400$ per
#month, plus 20$ multiplied by the number of years employed, plus 30$ for each child they have.
#Create a program that:
#     ● Reads the number of years employed
#     ● Reads the number of children the employee has
#     ● Prints the total amount of salary the employee makes
#         Output: "The total amount is 560$. 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids"

#                  Solution: USING PROCEDURAL PROGRAMMING

# Declaring the required variables

minimum_wage = 400  # declaring minimum wage per month
yearly_increment = 20
child_bonus = 30

# prompting the user to enter the number of years employed and number of children as integer
number_of_years = int(input("Enter the number of years employed: "))
number_of_children = int(input("Enter the number of children that you have: "))

# computing the total salary
total_salary = minimum_wage + (yearly_increment * number_of_years) + (child_bonus * number_of_children)  
print("Your total salary is = : $", total_salary)


