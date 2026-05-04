"""Generate 20 random integers and store them in a list. Accept a number from the
user and print position of all occurrences of that number in the list."""

import random


numbers = []

for i in range(20):
    n = random.randint(1,50)
    numbers.append(n)

print("List of 20 random integers:")
print(numbers)


# Accept number from user
x = int(input("Enter number to search: "))

print("Positions of the number are:")

for i in range(20):
    if numbers[i] == x:
        print(i)