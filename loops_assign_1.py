# write a program in why loop and for loop that determines if a number is odd or even in the range 1-10

#  FOR LOOP

# using array of numbers
print(" This is a FOR LOOP")
num = [1,2,3,4,5,6,7,8,9,10]
for x in num:
    if(x %2 == 0):
        print(x, ": is even")
    else:
        print(x, ": is odd")
    
# using the rang() method
print(" This is a FOR LOOP")

for i in range(1, 10):
    if(i %2 == 0):
        print(i, ": is an even number")
    else:
        print(i, ": is an odd number")
        
#   WHILE LOOP
print(" This is a WHILE LOOP")

number = 1
while(number <= 10):
    if(number %2 ==0):
        print(number, ": is an Even number")
    else:
        print(number, ": is an Odd number")
    number += 1