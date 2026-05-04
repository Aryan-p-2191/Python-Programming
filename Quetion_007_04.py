'''Write a program that reads a string from the keyboard and creates dictionary containing 
frequency of each character occurring in the string. '''

string=input("Enter a string:")
freq={}
for ch in string.upper():
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)