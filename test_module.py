import python_custom_module as custom

#  python module to output a name
print("python module to output a name")
print(custom.my_name("Mbulle"))

#  python module to check if a number is Even or Odd
custom.odd_even(9)

#  python module to check if a number entered by a user is PRIME or NOT
import prime_number as p

print("Checking if a number entered by a user is PRIME or NOT")
p.is_prime(
    int(input("Enter a number to check if its prime or not: ")))


#     METHOD 2:Using a return statement
#    For the user to see the output when we use the "return" type statement, we use the print statement 

print(p.is_prime2(
    int(input("Enter a number to check if its prime or not for method 2: "))))