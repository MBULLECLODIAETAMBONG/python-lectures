#                            Exercise 4
#  Create a program that reads a number that you want to get the sum until that number
#  Create a program that:
#         ● Reads the number you want to sum
#         ● Calculates the sum of 1+2+3+4...+98+99+n
#         ● Prints the sum of 1+2+3+4...+98+99+n
#       Input example: 100
#               Output: "The sum is 5050"


#       Solution: Using FUNCTIONAL PROGRAMMING


def sum_of_number():
    
    number = int(input("Enter a number that you want to get the sum until that number: "))
    
    # initializing sum to zero
    sum = 0
    
    # using a for loop to iterate through the value entered
    for num in range(1, number+1):
        sum = sum + num
    return sum

