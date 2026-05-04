'''08.Check whether a triangle is valid or not, when the three 
angles of the triangle are entered through the keyboard. A triangle
is valid if te sum of all the three angles is equal to 180 degrees.'''
a1 = int(input("Enter an angle teiangle"))
a2 = int(input("Enter an angle teiangle"))
a3 = int(input("Enter an angle teiangle"))
if a1+a2+a3 == 180:
    print("valid")
else:
    print("not valid")    