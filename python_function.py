# Writing a parameterless function in python

def my_name():    # function name 
    print("My name is CLODIA, am a DevOp Engineer")  # function body
print(my_name())  # function call

# Parameeter FUnction

def my_identity(name, address, birthday):
    print("Hello my name is", name, "Welcome to Compudamy")
    print("I live in", address)
    print("I was born in", birthday)
my_identity("CLODIA", "CAMEROON", "02-06-2000")

# Write a function that outputs if a number is odd or even

def num_odd_or_even(x):
    if (x %2 ==0):
        print(x, ":is Even")
    else:
        print(x, ": is odd")
num_odd_or_even(3)

# Write a function that prompts a user to input a number and  determines that outputs if a number is odd or even
def num_odd_or_even(x):
    if (x %2 ==0):
        print(x, ":is Even")
    else:
        print(x, ": is odd")
num_odd_or_even(int(input("Enter any number :")))
    