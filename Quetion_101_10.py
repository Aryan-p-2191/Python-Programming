'''Write a program that defines a function called frequency() which computes the frequency of
words present in a string passed to it. The frequencies should be returned in sorted order
of words in the string.'''

def frequency(str):
    freq = {}
    for i in str.split():
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
        return dict(sorted(freq.items()))
str = input("Enter a string: ")
print(frequency(str))