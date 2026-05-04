'''Generate 30 random numbers and put them in a list. Create two more lists
one containing only +ve numbers and another with 1ve nos.'''

import random

random_list=[]
while len(random_list)<30:
    num=random.randint(-50,50)
    random_list.append(num)
print("List of 30 random numbers:")
print(random_list)

negative_num=[]
positive_num=[]
count=0
for i in random_list:
    if i==0:
        count+=1
    else:
        if i<0:
            negative_num.append(i)
        else:
            positive_num.append(i)

print(f"in list {count} number is zero.")
print("negative number list:")
print(negative_num)
print('positive numbers list:')
print(positive_num)