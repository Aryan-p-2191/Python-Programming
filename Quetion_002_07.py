'''07.Accept a year value from the user. Check whether it is a leap
year or not.'''
year = int(input("Enter year:"))
if (year%100!=0 and year%4==0) or year%400==0:
    print(f"{year} is leap year")
else:
    print(F"{year} is not leap year")