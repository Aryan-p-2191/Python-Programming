'''A list contains some negative and some positive values. Write a recursive function that sanitizes the list by 
replacing all negative numbers with 0.'''

def sanitize_list(lst):
    if len(lst) == 0:
        return []
    else:
    
        for i in lst:
            if i < 0:
                i = 0
            return [i] + sanitize_list(lst[1:])     
        
numbers = [1, -2, 3, -4, 5]
sanitized_numbers = sanitize_list(numbers)  
print(sanitized_numbers)