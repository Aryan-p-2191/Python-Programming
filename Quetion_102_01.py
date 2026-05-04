'''If a positive integer is entered through the keyword, write a recursive function to 
obtain the prime factors of the number. '''

def prime_factors(n, factors=None):
    
    if factors is None:
        factors=[]
    
    if n<2:
        return factors
    
    for i in range(2,n+1):
        if n%i == 0:
            factors.append(i)
            return prime_factors(n//i,factors)

n=int(input("Enter an positive numbers:"))
result = prime_factors(n)
print(result)        