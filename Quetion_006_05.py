"""Remove empty tuple(s) from the list of tuples."""

l = ["aryan",(),25,(25,36,3,62,5),"meet"]
new_l=[]
for i in l:
    if i != ():
        new_l.append(i)
print(new_l)
