#       EXERCISE

#The idea is for you to develop a Python script that allows users to select the deployment environment
# (e.g., development, staging, or production) and performs different actions based on their choice. 

# Use conditionals to check the selected environment and execute specific deployment tasks accordingly. 

# This exercise will allow you to practice conditionals, function calls that we studied in the last 
# lecture and code organization to automate the deployment process based on user inputs.



#  SOLUTION OF SCENARIO.TXT
# Algorithm

# step1:
# -propose a function to deploy to development
# -propose a function to deploy to staging
# -propose a function to deploy to production
# -Deploy to the environment based on conditions

# Step2:
# -Prompt the user to input the deployment environment

# Step3:
# -Call the deploy function

#  CODE

def deploy_to_development():
    print("deploying to development environment")

# propose a function to deploy to staging environment


def deploy_to_staging():
    print("deploying to staging environment")

# Propose a function to deploy to production environment


def deploy_to_production():
    print("deploy to production environment")


def deploy(environment):
    if environment == "development":
        deploy_to_development()

    elif environment == "staging":
        deploy_to_staging()

    elif environment == "production":
        deploy_to_production()
    else:
        print("Its an invalid environment. Please choose either staging, production or development")
        

# Prompt the user for the deployment environment
user_environment = input(
    'Enter the deployment environment(development, staging, production): ')

# Call the function with user's choice
deploy(user_environment)