# A MODULE: is a file that contains code that performs a specific task when called.
# There are two main types of Python modules: built-in modules and user-defined modules

#               EXERCISE
# Build a custom python module called math_utils.py that provides basic math operations. 
# Implement functions like add(a,b), subtract(a,b), multiply(a,b)and divide(a,b). In your main scripts, 
# import the math_utils modules and perform calculations using the defined math functions.

#                SOLUTION

# Python Module addition

def add(a, b):

   addition = a + b
   return addition

a = add(
    int(input("Enter the value of a for addition: ")),
    int(input("Enter the value of b addition: "))
)



# Python Module subtraction

def subtract(a,b):
    
   subtraction = a - b 
   return subtraction

s = subtract(
    int(input("Enter the value of a for subtraction: ")),
    int(input("Enter the value of b for subtraction: "))
)
# Python Module multiplication

def multiply(a, b):
    
    multiplication = a * b
    return multiplication

m = multiply(
    int(input("Enter the value of a for multiplication: ")),
    int(input("Enter the value of b for multiplication: "))
)

# Python Module division

def divide(a,b):
    
    division = a / b
    return division

d = divide(
    int(input("Enter the value of a for division: ")),
    int(input("Enter the value of b for division: "))
)

# examples



