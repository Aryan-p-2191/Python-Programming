'''Write a program that defines a function count_lower_upper() that accepts a string and 
calculates the number of uppercase and lowercase alphabets in it. It should return these 
values as a dictionary. Call this function for some sample string.'''

string=input("Enter an string:")

def count_lower_upper(string):
    lower=0
    upper=0
    for i in string:
        if i.isupper():
            upper+=1
        elif i.lower():
            lower+=1
    return {f"lower = {lower},upper = {upper}"} 

print(count_lower_upper(string))
