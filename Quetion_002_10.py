l = float(input("Enter length of rectangle"))
b = float(input("Enter breadth of rectangle"))

a=l*b
p=2*(l+b)

if a>p:
    print("Area is greater then perameter")
else:
    print("Area is less then perameter")
print(a)
print(p)

