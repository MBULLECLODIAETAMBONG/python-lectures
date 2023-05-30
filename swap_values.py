#                 EXERCISE
# Create two variables x and y, and initially set them each to a different number. Write a python script that swaps both values.

# Example: x = 10, y = 20
# Output: x = 20, y = 10

#             SOLUTION

#       METHOD 1: Using swap variable as a temporary variable

X = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print("The values of x and y before swapping is:", X, y)
s = X
X = y
y = s
print("The value of x is: ", X)
print("The value of y is: ", y)


#      METHOD 2: Without using swap variable

X = int(input("Enter the value of x for method 2: "))
y = int(input("Enter the value of y for method 2: "))

X, y = y, X

print("The value of x is: ", X)
print("The value of y is: ", y)

#      METHOD 3:  Using a Function
#swap=0
def swap_value(x, y):
    swap = x
    x = y
    y = swap
    return x, y
numbers = swap_value(
    int(input("enter the value of x for method 3: ")),
    int(input("enter the value of y for method 3: ")))

print(numbers)
    
