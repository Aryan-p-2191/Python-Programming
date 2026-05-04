'''Delete an element of a tuple by creating a new tuple.'''

t=(25,23,2,1,26,24)

t=t[0:2]+t[3:]
print(t)