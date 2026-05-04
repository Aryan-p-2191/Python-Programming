"""Create a list of 5 odd integers using random nos. Similarly create a list of 4 
even integers using random nos. Replace the third element of odd integers with  a 
list of 4 even integers. Flattern, sort and print the list. Provide appropriate 
message at each stage."""

import random

odd_list=[]
while len(odd_list)<5:
    num = random.randint(1,50)
    if num % 2!=0:
        odd_list.append(num)
        
print("List of 5 random odd integers:")
print(odd_list)

even_list=[]
while len(even_list)<4:
    num = random.randint(1,50)
    if num % 2==0:
        even_list.append(num)

print("List of 4 random even integers:")
print(even_list)

odd_list[2]= even_list
print("after replace 3rd element of odd_list")
print(odd_list)

flat_list=[]

for item in odd_list:
    if isinstance(item,list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

print("Flattern list:")
print(flat_list)

flat_list.sort()
print("shorted list:")
print(flat_list)