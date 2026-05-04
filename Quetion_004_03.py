'''03.Count no. of alphabets and no. of digits 
in any given string.'''

str=input("Enter a string:")
digits=0
alphabets=0
spacial_character = 0
for i in range(0,len(str)):
    ch = str[i]
    if '0'<= ch <='9':
        digits+=1
    elif ord(str[i].lower()) in range((ord('a')),(ord('z')+1)):
        alphabets+=1
    else:
        spacial_character+=1
print(f"didits = {digits}")
print(f"alphabets = {alphabets}")
print(f"spacial character = {spacial_character}")


        
