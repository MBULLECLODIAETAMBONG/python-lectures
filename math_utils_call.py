#  A MODULE: is a file that contains code that performs a specific task when called.
#There are two main types of Python modules: built-in modules and user-defined modules

# importing the module created call "math_utils" into my program file (math_utils_call.py)

import math_utils
import math

# Python Module addition
# math_addition= math_utils.add(4, 8)

math_addition= math_utils.a
print("The Addition is: ", math_addition)

# Python Module subtraction
#math_subtraction = math_utils.subtract(4, 8)

# making the subtraction dynamic
math_subtraction = math_utils.s
print("The Subtraction is: ", math_subtraction)

# Python Module multiplication
# math_multiplication = math_utils.multiply(4, 8)

math_multiplication = math_utils.m
print("The Multiplication is: ", math_multiplication)

# Python Module division
# math_division = math_utils.divide(4, 8)

math_division = math_utils.d
print("The Division is: ", math_division)


#  to get the square of a number we use the isqrt() method
print(math.isqrt(9))


