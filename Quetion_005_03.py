'''Generate 50 random numbers in the range 1 and 30. Remove all duplicate values 
from the list.'''

import random
random_list=[]
while len(random_list)<50:
    num = random.randint(1,30)
    random_list.append(num)
print("List of random numbers:")
print(random_list)
s=set(random_list)

print("removebal duplicate values list:")
print(list(s))