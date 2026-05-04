'''01.Print largest and smallest values out of two.'''

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))

if a>b:
    print("largest =", a,"smallest =" ,b)
    # print(f"largest = {a},smallest = {b}")
elif b>a:
    print(f"largest = {a},smallest = {b}")
else:
    print("both number are same")
