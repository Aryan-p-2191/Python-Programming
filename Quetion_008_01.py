'''Two students choose subjects represented as sets:
       s1 = {'Math', 'Physics', 'Chemistry'} and s2 = {'Physics', 'Biology', 'Math'}
       Write a program to:
1.Find common subjects.
2.Find subjects taken by only first student.
3.Find subjects taken by only second student.
4.Find total unique subjects.
'''
s1 = {'Math', 'Physics', 'Chemistry'} 
s2 = {'Physics', 'Biology', 'Math'}
print(f"common subjects are :{s1&s2}")
print(F"subjects taken by only first student:{s1-s2}")
print(F"subjects taken by only second student:{s2-s1}")
print(F"total unique subjects:{s1|s2}")
