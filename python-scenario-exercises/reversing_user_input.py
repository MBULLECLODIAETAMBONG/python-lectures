"""
    Write a loop in python that will keep reversing user's input until he enters te letter "q" to quit
"""

#      SOLUTION: Using Procedural programming

#        1. Reversing using SLICING "[::-1]"

user_input = str(input("Enter any word of your choice!  "))
# split actually split/separate the sentences into st of words (each word as a string in a list) and [::-] using slicing
word = user_input.split()[::-1]
for i in word:
    
    if user_input != "q":
        print(i)
        
    else:
        break 
       