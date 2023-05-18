# write a function in python that checks two parameters and check the divisibility between the number and output if the numbers are divisible by each 
# hint the numbers are divisible if the reminder between the two numbers should be equal to zero

def check_divisibility(x, y):
   
    if (x % y and y % x ==0):
        print(x, "and", y, ": are Divisible by each other")
        
    else:
        print(x, "and", y, ": are NOT Divisible by each other")
        
check_divisibility(int(input("Enter any number :")),
                   int(input("Enter any number :")))


# method two
print("This is a different method")
def check_divisibility(x, y):
   
    if (x % y == 0):
        print(x, "and", y, ": are Divisible by each other")
        
    else:
        print(x, "and", y, ": are NOT Divisible by each other")
        
check_divisibility(int(input("Enter any number :")),
                   int(input("Enter any number :")))