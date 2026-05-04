'''04.Check whether a given number is prime, is perfect, is 
Armstrong, is palindrome, is automorphic'''

n=int(input("Enter a num:"))
# FOR PRIME NUMBERS:
flag = True
if n>1:
    for i in range(2,n):
        if n % i == 0 :
            flag = False
            break
        else:
            flag = True
else:
    flag=False
if flag:
    print(f"{n} is prime number.")
else:
    print(f"{n} is not prime number.")


# FOR PERFECT NUMBERS:   

sum_of_divisor=0
for i in range(1,n):
    if n % i == 0:
        sum_of_divisor+=i
if sum_of_divisor==n:
    print(f"{n} is perfect number.")
else: 
    print(f"{n} is not perfect number.")


# FOR ARMSTRONG NUMBERS:

num_str=str(n)
power = len(num_str)

armstrong_sum=0

for i in num_str:
    armstrong_sum+=int(i)**power

if armstrong_sum == n:
    print(f"{n} is armstrong number.")
else:
    print(f"{n} is not armstrong number.")

# FOR PAlINDROME NUMBERS:

if num_str==num_str[::-1]:
    print(F"{n} is palindrome number.")
else:
    print(F"{n} is not palindrome number.")

# FOR AUTOMORPHIC NUMBERS:

squere = n**2

if str(squere).endswith(num_str):  
    print(f"{n} is automorphic number.")
else:
    print(f"{n} is not automorphic number.")
