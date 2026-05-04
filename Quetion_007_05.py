'''Create two dictionaries - one containing grocery items and their prices and another 
containing grocery items and quantity purchased. By using the values from these two 
dictionaries compute the total bill.'''

prices = {
    "rice": 50,
    "wheat": 40,
    "sugar": 45,
    "milk": 67
}
quantity = {
    "rice": 2,
    "wheat": 3,
    "sugar": 1,
    "milk": 2
}
total=0

for item in prices:
    total+=prices[item]*quantity[item]
print(f"total = {total}")
