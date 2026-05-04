'''Write a program that defines a function convert() that receives a string containing a
sequence of whitespace separated words and returns a string after removing all duplicate 
words and sorting them alphanumerically. Hint: use set(), list () , sorted(), join().'''

def convert(s):
    word = list(set(str(s).split()))
    word = word.sort()
    result = " ".join(word)
    return result

s=input("Enter a string:")
result=convert(s)
print(result) 