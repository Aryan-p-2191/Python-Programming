'''Count how many vowels are there in a string. Accept the string from the user.'''
str=input("Enter your string:")

l=['a','e','i','o','u']

count=0
for j in range(0,len(str)):
    if str[j].lower() in l:
        count+=1
print(f'{count} vowels are in the string')        