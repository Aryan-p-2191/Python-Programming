'''02.Print largest and smallest values out of three.'''
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))

if a==b==c:
    print("All numbers are same.")
else:
    if a>b and a>c:
        print(f"largest = {a}")
    elif a<b and b>c:
        print(f"largest = {b}")
    else :
        print(f"largest = {c}")

    if a>b and c>b:
        print(f"smallest = {b}")
    elif a<b and a<c:
        print(f"smallest = {a}")
    else :
        print(f"smallest = {c}")
    