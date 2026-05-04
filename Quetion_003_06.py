'''Write a program to: Concatenate two strings entered by the user 
and Repeat the concatenated string n times, where n is user input'''

str1=input("Enter your string 1:")
str2=input("Enter your string 2:")
n=int(input("Enter value of n:"))
str=str1+str2
print(f"{n*str}")