'''Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find 
the number of days between the two dates.'''

from datetime import date

d1, m1, y1 = map(int, input("Enter first date (d m y): ").split())
d2, m2, y2 = map(int, input("Enter second date (d m y): ").split())

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

print(f"Days = {abs((date2 - date1).days)}")