'''A Python program to access each element of a string in 
forward and reverse orders using while loop. '''

str=input("Enter a string:")
print("forward order:")
i=0
while i < len(str):
    print(str[i],end=" ")
    i+=1
print("\nreverse order:")
i=len(str)-1
while i>=0:
    print(str[i],end=" ")
    i-=1
