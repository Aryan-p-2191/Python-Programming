'''Write a program that defines a function count_alpha_digits() that accepts a string and 
calculates the number of alphabets and digits in it. It should return these values as a 
dictionary.'''

def count_alpha_digits(s):
    alpha=0
    digits=0
    for i in s:
        if i.isalpha():
            alpha+=1
        elif i.isdigit():
            digits+=1
    return {f"Alphabets={alpha},Digits={digits}"}
 
s=input("Enter a string:")
result = count_alpha_digits(s)
print(result)
