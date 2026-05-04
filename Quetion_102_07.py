'''Write a recursive function to obtain average of all numbers present in a given list.'''

def sum_list(_list):
    sum=0
    if len(_list)==0:
        return 0
    sum=_list[0]+sum_list(_list[1:])
    return sum  
# hear first difine sum function after make that divison by the len of list#

numbers=[1,2,3,4,5]
average=sum_list(numbers)/len(numbers)          
print("Average of the list is:",average)
