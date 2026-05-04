'''01.Print all alphabets in upper case and in lower case.'''

print("upper case alphabets:")
for al in range(ord('a'),ord('z')+1):
    print(chr(al),end=" ")
print("lower case alphabets:")
for al in range(ord('A'),ord('Z')+1):
    print(chr(al),end=" ")
