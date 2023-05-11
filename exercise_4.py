# Write an if statement that asks for the user's name via input() function.
# If the name is “Acha” make it print "Welcome on board Acha” Otherwise make it print "Good morning Engr. Akum

name = str(input("Enter any name: "))

# checking if name is equal to Acha
if(name == "Acha"):
    print("Welcome on board Acha")
else:
    print("Good morning Engr.", name)