# Propose a program to calculate Simple Interest.
# Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate

# Get the value of Principal from the user
P = float(input("Enter the principal: "))
print("p = ", P, \n)
# Get the value of Time from the user
T = float(input("Enter the Time: "))
# Get the value of Rate from the user
R = float(input("Enter the Rate: "))
# formula for simple interest
simple_interest = (P * T * R)/100
print("The simple interest is: ", simple_interest)
