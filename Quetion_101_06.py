'''Write a function to create and return a list containing tuples of the form (x,x2,x3) 
for all x between 1 and given ending value (both inclusive).'''

def creat_tuple(n):
    result=[]
    for i in range(1,n+1):
        result.append((i,i**2,i**3))
    return result

n=int(input("Enter value of n:"))

print(f"Result:{creat_tuple(n)}")