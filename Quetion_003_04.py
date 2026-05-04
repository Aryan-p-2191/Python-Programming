'''Write a program that Accepts a string from the user and 
Prints: First character, Last character, and Middle character 
(if length is odd)'''

str=input("Enter a string:")
l=len(str)
if l%2==0:
    print(str[0],str[l-1])
else:
    print(str[l//2]) 

