'''A palindrome is a word or phrase that reads the same in both directions. Write a program
that defines a function ispalindrome() which checks whether a given string is a palindrome
or not. Ignore spaces and case mismatch while checking for palindrome.'''

n=int(input("Enter value of n:"))

def ispalindrome(n):
    if str(n)==str(n)[::-1]:
        return (f"{n} is palindrome number")
    else:
        return (f"{n} is not palindrome number")
    
print(ispalindrome(n))