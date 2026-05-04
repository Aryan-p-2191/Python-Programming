'''Print nCr and nPr.'''

n = int(input("Enter value of n:"))
r = int(input("Enter value of r:"))

if r>n or n<0 or r<0:
    print("Invalid input:")
else:
    fact_n=1
    for i in range(1,n+1):
        fact_n*=i
    fact_r=1
    for i in range(1,r+1):
        fact_r*=i
    fact_nr=1
    for i in range(1,n-r+1):
        fact_nr*=i
nCr = fact_n//(fact_nr*fact_r)   
nPr = fact_n//fact_nr

print(f"nCr={nCr}")
print(f"nPr={nPr}")
