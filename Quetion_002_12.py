'''12.Given the coordinates (x,y) of center of a circle and its 
radius, determine whether a point lies inside the circle, on the 
circle or outside the circle. (Hint: Use sqrt( ), pow( ) )'''

h = float(input("Enter centen x(h):"))
k = float(input("Enter centen y(k):"))

r = float(input("Enter redius r:"))

x = float(input("Enter point x:"))
y = float(input("Enter point y:"))

d= ((x-h)**2 + (y-k)**2)**(1/2)

if d==r:
    print(f"{(x,y)} point on the circle")
elif d<r:
    print(f"{(x,y)} point inside circle")
else:
    print(f"{(x,y)} point outside circle")