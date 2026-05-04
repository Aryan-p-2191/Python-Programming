'''A list contains tuples containing roll no., name and age of student. Write a python 
program to create three lists separately for roll no., name and ageA list contains tuples 
containing roll no., name and age of student. Write a python program to create three 
lists separately for roll no., name and age'''

list = [
    (101,"aryan",19),
    (102,"jiya",18),
    (103,"yug",18),
    (104,"veer",18),
    (105,"kunj",19),
    (106,"Shravan",17)
]
roll_no_list=[]
name_list=[]
age_list=[]

for i in list:
    roll_no_list.append(i[0])
    name_list.append(i[1])
    age_list.append(i[2])

print(f"Roll number list:{roll_no_list}")
print(f"Name list:{name_list}")
print(f"Age list:{age_list}") 
