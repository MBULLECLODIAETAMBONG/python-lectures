list_of_members = ["Richard", "Akenji", "Mbulle", "Miriam","Sandra", "Lydwin", "Mirabel", "Edna","Paul", "Pearl"]
hourly_rate_member = 2
hourly_rate_non_member = 5

tax_rate_for_member = 0.1
tax_rate_for_non_member = 0.2

hours_user_spent =int(input("Enter the hours spent: "))

member_entered = str(input("Enter the name of the member ?: "))

for member in list_of_members:
    
    if member_entered == "Richard" or "Akenji" or "Mbulle"  or "Miriam" or "Sandra" or "Lydwin" or "Mirabel" or "Edna" or "Paul" or "Pearl":
        hourly_rate = hourly_rate_member
        tax_rate = tax_rate_for_member
        membership_status = member, "is a member"
        
    else:
        hourly_rate = hourly_rate_non_member
        tax_rate = tax_rate_for_non_member
        membership_status =  member, "is a member"
        
total_amount = hours_user_spent * hourly_rate
tax_fee = total_amount * tax_rate
total_amount += tax_fee

print(membership_status, total_amount)
# print(membership_status, "stayed", hours_user_spent, "hours for", hourly_rate, "$/hour","plus the", tax_rate, "the total amount is: ", total_amount)
