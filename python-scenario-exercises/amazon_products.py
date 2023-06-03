#                 Exercise 3
# You want to buy something from Amazon. The seller charges different prices for shipping cost
# based on location. For US it's 5$ for Europe it's 7$ for Canada it's 3$ for other places it's 9$
# Create a program that:

#       ● Reads the cost of the product
#       ● Reads your location
#       ● Print the amount of money you have to pay
#  Output: "You have to pay 23$, 20$ for the product and 3$ for shipping cost

#         Solution: USING PROCEDURAL PROGRAMMING

# method are invoked in front of a class or tied down to a class or variable whereas functions are independent

#  initializing different location
US = 5
Europe = 7
Canada = 3
other_places = 9

#  prompt the seller to enter the cost of the product
cost_of_product = float(input("What is the cost of this product? : "))

# total_cost_of_product = (cost_of_product + US) or (cost_of_product + Europe) or (cost_of_product + Canada) or (cost_of_product + other_places)   

# prompt the customer to enter the location
location = str(input("Enter your location (US, Europe, Canada or Other places)"))

if (location.upper() == "US"):
    
    # calculates the total cost of the product by adding cost of product plus shipping cost base on customer location
    shipping_cost = 5
   
elif(location.upper() == "EUROPE"):
    
    # calculates the total cost of the product by adding cost of product plus shipping cost base on customer location
    shipping_cost = 7
    
elif(location.upper() == "CANADA"):
    
    # calculates the total cost of the product by adding cost of product plus shipping cost base on customer location
    shipping_cost = 3
        
else:
    
    # calculates the total cost of the product by adding cost of product plus shipping cost base on customer location
    shipping_cost = 9
    
total_cost_of_product = (cost_of_product + shipping_cost)
print("You have to pay", total_cost_of_product,"$,", cost_of_product,"$", "for the product and",other_places,"$ for shipping cost")