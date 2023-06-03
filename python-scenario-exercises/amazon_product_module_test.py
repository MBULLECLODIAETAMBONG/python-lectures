# importing the only the function from the user defined module created in the file call "amazon_product_module.py" here.

from  amazon_product_module import buy_product

#  prompt the seller to enter the cost of the product
cost_of_product = float(input("What is the cost of this product? : "))

# total_cost_of_product = (cost_of_product + US) or (cost_of_product + Europe) or (cost_of_product + Canada) or (cost_of_product + other_places)   

# prompt the customer to enter the location
location = str(input("Enter your location (US, Europe, Canada or Other places)"))

# calling the function from the amazon_product_module
print(buy_product(location, cost_of_product))

