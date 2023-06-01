#                            Exercise 4
#  Create a program that reads a number that you want to get the sum until that number
#  Create a program that:
#         ● Reads the number you want to sum
#         ● Calculates the sum of 1+2+3+4...+98+99+n
#         ● Prints the sum of 1+2+3+4...+98+99+n
#       Input example: 100
#               Output: "The sum is 5050"

#     Solution: PROCEDURAL PROGRAMMING

#                    Using  FOR LOOP

# prompt a user to enter the number he/she wants to get the sum
number = int(input("Enter a number that you want to get the sum until that number: "))

# initializing sum to zero
sum = 0

# using a for loop to iterate through the value entered
for num in range(1, number+1):
    sum = sum + num
print("The sum of all numbers till number entered is: ", sum) 


#                       Using  WHILE  LOOP

# initializing num to zero since the programs says we begin addition from 1 and not zero (1+2+3+4...+n)
num = 1

# initializing sum to zero
sum = 0

# using a for loop to iterate through the value entered
while(num <= 100 ):
    
    sum = sum + num
    num += 1
print("The sum of all numbers is: ", sum) 

   