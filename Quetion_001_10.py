'''Convert dollars into pound where 1 $ = 48 Rs.
And 1 pound = 70 Rs'''
dollars = int(input("Enter amount in dollars:"))
rupees = dollars*48
pound = rupees/70
print(f"Rs. = {rupees},pound = {pound}")
