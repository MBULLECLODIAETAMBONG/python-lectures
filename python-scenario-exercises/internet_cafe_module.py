#                      Exercise 2
# An internet cafe has 2 ways of charging. If the user is a member pays 2$/hour, Else the user
# pays 5$. Find if someone is a member or not and calculate the price based on how many hours
# the user spend. If the user is a member the tax is 10% else the tax is 20%.
# Create a program that:
#      ● Reads how many hours the user spend
#    ● Check if is a member
#    ● Add the proper tax fee
#    ● Print the total amount the user has to pay
#        Output: "The user is a member stayed 2 hours for 2$/hour plus the 10% the total amount is 4.4$


#                Using functional programming

#  declaring the appropriate variables 

def check_member():
    
    hourly_rate_member = 2
    hourly_rate_non_member = 5

    tax_rate_for_member = 0.1
    tax_rate_for_non_member = 0.2

    hours_user_spent =int(input("Enter the hours spent: "))

    is_a_member = str(input("Are you a member ?: "))
    if is_a_member.lower() == "yes":
        hourly_rate = hourly_rate_member
        tax_rate = tax_rate_for_member
        membership_status = "The user is a member"
        
    else:
        hourly_rate = hourly_rate_non_member
        tax_rate = tax_rate_for_non_member
        membership_status = "The user is NOT a member"
        
    total_amount = hours_user_spent * hourly_rate
    tax_fee = total_amount * tax_rate
    total_amount += tax_fee
    return total_amount
