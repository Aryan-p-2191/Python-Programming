'''Calculate ab where a and b received through the keyword using recursion.'''

def power(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / power(a, -b)
    else:
        return a * power(a, b - 1)
    
a = int(input("Enter a value of a: "))        
b = int(input("Enter a value of b: "))
result = power(a, b)
print(f"{a} raised to the power of {b} is: {result}")