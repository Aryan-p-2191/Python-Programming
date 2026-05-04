'''Write a program that defines a function compute() that calculates the value of 
n + nn + nnn + nnnn, where n is digit received by the function. test the function for 
digits 4 to 7.'''

def compute(n):
    return n+n*11+n*111+n*1111
for i in range(4,8):
    print(f"for {i}:{compute(i)}")