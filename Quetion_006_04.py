'''Create a list of tuples containing a food item and its price. Sort the tuples in 
descending order by price.'''

food = [("Pizza",250), ("Burger",120), ("Pasta",200), ("Dosa",60)]

food.sort(key = lambda x:x[1] ,reverse=True)

print(food)