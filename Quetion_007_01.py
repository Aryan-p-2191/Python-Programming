'''Write a program to create three dictionaries and concatenate them to create fourth 
dictionary.'''

d1={'aryan':50,'shravan':20}
d2={'swati':30,'chintan':80}
d3={'yug':70,'veer':90}

d4 = {**d1,**d2,**d3}
# d4.update(d1)
# d4.update(d2)
# d4.update(d3)
print(d4)