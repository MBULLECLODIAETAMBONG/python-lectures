# Write a Python script that prompts the user to enter a password and then checks the strength
# of the password based on predefined criteria. A password is considered strong if:
#    8 characters length or more
#    1 digit or more
#    1 symbol or more
#    1 uppercase letter or more
#    1 lowercase letter or more

#The script should provide feedback on the strength of the password using a combination of conditions and loops.

password_check = str(input("Enter your password: "))

if (len(password_check) >= 8):
    print("Your Password is strong")
    
else:
    print("Your Password is weak")
    
 
 
#  METHOD 2
print("METHOD 2")       
        
def password_check(your_password):
    
    for p in your_password:
        
        if not (len(your_password) >= 8  and (p.isalnum())):
           
            print("Your Password is weak")
                        
        else:
            print("Your Password is strong")
            
password_check(str(input("Enter your password: ")))
