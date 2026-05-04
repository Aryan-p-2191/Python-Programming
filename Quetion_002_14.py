'''14)	Accept marks of three subjects. Print total and average 
along with whether a candidate has passed or fail. If student
secures <= 39 marks in any subject, consider him as fail. Also  
assigned a subject wise grade based on the following table:

Marks Range	Grade
Absent  	NA
00 - 39 	F
40 - 44 	P
45 - 49 	C
50 - 54 	B
55 - 59 	B+
60 - 69 	A
70 - 79	    A+
80 - 100	O
'''
attendence = input("mark your attendence:")
if attendence=="absent":
    print("grade=NA")
elif attendence == "present":    
    s1=int(input("Enter subject 1 marks:"))
    s2=int(input("Enter subject 2 marks:"))
    s3=int(input("Enter subject 3 marks:"))

    total =s1+s2+s3
    avg = float(total/3)

    if 0<=avg<=39:
        print("grade = F")
    elif 40<=avg<=44:
        print("grade = P")
    elif 45<=avg<=49:
        print("grade = C")
    elif 50<=avg<=54:
        print("grade = B")
    elif 55<=avg<=59:
        print("grade = B+")
    elif 60<=avg<=69:
        print("grade = A")
    elif 70<=avg<=79:
        print("grade = A+")
    elif 80<=avg<=100:
        print("grade = O")
    else:
        print("something error")
else:
    print("something error")
