'''11.Given three points (x1,y1), (x2,y2) and (x3,y3), check if
 all the three points fall on one straight line.'''

x1 = float(input("Enter x1 :"))
y1 = float(input("Enter y1 :"))

x2 = float(input("Enter x2 :"))
y2 = float(input("Enter y2 :"))

x3 = float(input("Enter x3 :"))
y3 = float(input("Enter y3 :"))

if x2*y3-y2*y3+y1*x3-x1*y3+x1*y2-y1*x2 == 0:
    print("collenear.")
else:
    print("not collenear.")