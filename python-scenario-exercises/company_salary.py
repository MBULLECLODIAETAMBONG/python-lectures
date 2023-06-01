#  Given criteria for computation

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


