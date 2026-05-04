'''A list contains names of boys and girls as its elements. Boys
names are stored as tuples. Write a program to find out number of 
boys and girls in the list. (Hint: use isinstance(ele,tuple))'''

list=['riya','jiya','siya',('dev',),('jeet',),('meet',)]
boys=0
girls=0
for i in list:
    if isinstance(i,tuple):
        boys+=1
    else:
        girls+=1
print(f"boys={boys}")
print(f'girls={girls}')
