'''13)	Convert number 0 to 19 to its equivalent words. 
E.g. 0 => zero, 19=>nineteen.'''
n = int(input("Enter a number (0-19): "))

words = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine",
         "ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

if 0 <= n <= 19:
    print(words[n])
else:   
    print("Number out of range")
