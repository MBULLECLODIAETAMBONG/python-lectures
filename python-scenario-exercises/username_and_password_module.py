#                        Exercise 5
#  Create a program that register a user with a username and a password. Then the user will try to
#  login with the login credentials. If the user make 3 wrong attempts exit program with proper message.
#  Create a program that:
#      ● Reads the username and the password
#      ● Then the user try to login
#      ● If the user makes 3 wrong attempts exit with proper message


#               Solution:  FUNCTIONAL PROGRAMMING

def login_credentials():
    
    # initializing trial to be zero
    trial = 0
    
    # trial should be less than 3 since trial begins from zero making it a maximum of three trials
    while(trial < 3):
        
        # prompting the user to enter the username and password
        user_name = str(input("Enter your user name: "))
        password = str(input("Enter your password: "))
        
        # checking if the user name and password entered correspond to user name and password
        if(user_name == "Admin" and password == "admin@123"):
            print("Access granted")
            break
        
        else:
            print("Wrong Credential, try again")
            trial += 1
            
            if(trial == 3):
                print('Three wrong attempts thus access Denied')
        
 