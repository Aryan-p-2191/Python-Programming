'''Remove Duplicates from List Using Set.'''

list_1=[25,2,2,3,78,6,3,6,5,2,25,1,4,48,1,4,78,4,8,48,4,8,9,25]
new_list=[]
for i in list_1:
    if i in new_list:
        continue
    new_list.append(i)
print(new_list)