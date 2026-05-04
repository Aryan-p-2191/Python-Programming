'''Write a program that defines a function sum_avg() to accept marks of five subjects and
calculates total and average. It should return  directly both values.'''

s1 = int(input("Enter marks of subject:"))    
s2 = int(input("Enter marks of subject:"))    
s3 = int(input("Enter marks of subject:"))    
s4 = int(input("Enter marks of subject:"))    
s5 = int(input("Enter marks of subject:"))    

def sum_avg(s1,s2,s3,s4,s5):
    return (s1+s2+s3+s4+s5)/5

print(f"Avrage = {sum_avg(s1,s2,s3,s4,s5)}")