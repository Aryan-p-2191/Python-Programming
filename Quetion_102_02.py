'''A positive integer is entered through the keyboard. Write a function to 
find its binary equivalent of this number.'''

def decimal_to_binary(n):
    if n==1:
        return 1
    elif n==0:      
        return 0
    else:
        return decimal_to_binary(n//2) * 10 + n%2
    
n = int(input("Enter a positive integer: "))
result = decimal_to_binary(n)
print(result)

 