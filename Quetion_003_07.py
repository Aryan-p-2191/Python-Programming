'''Write a program that: Accepts a string and Prints: Total 
length,Count of vowels, and Count of consonants.'''

str=input("Enter a string:")
l = len(str)
print(f"Total length = {l}")

l=['a','e','i','o','u']

vowels=0
for j in range(0,len(str)):
    if str[j].lower() in l:
        vowels+=1
print(f'{vowels} vowels are in the string')   
consonants =  len(str)-vowels 
print(f'{consonants} consonants are in the string')  