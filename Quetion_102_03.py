'''A string is entered through the keyboard. Write a recursive function that counts
the number of vowels in this string.'''

str = input("Enter a srring:")
def count_vowels(s):
    if len(s) == 0:
        return 0
    else:
        for i in s.lower():
            if i in 'aeiou':
                return 1 + count_vowels(s[1:])
            else:
                return count_vowels(s[1:])
            
result = count_vowels(str)
print("Number of vowels in the string:", result)    