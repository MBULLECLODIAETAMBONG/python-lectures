#  write a function that checks if a number entered by a user is a prime number or not

def is_prime(num):
    if num < 2:
        print("Enter a num different from", num)
        #return False
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("The number", num, "is NOT a Prime number")
                break
        else:
            print("The number", num, "IS a Prime number")

#number = is_prime(
#    int(input("Enter a number to check if its prime or not: ")))

#print(number) calling this function as a module in the  file call "test module.py"


#  METHOD 2: Using the Return type

def is_prime2(num):
    if num < 2:
        return False
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
            
    
    