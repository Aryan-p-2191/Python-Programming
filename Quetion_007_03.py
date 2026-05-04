'''Create a dictionary with dept no, employee roll no. and salary. Find out department
wise min and maximum of salary.'''

data = {
    101: [(1, 25000), (2, 30000), (3, 20000)],
    102: [(4, 40000), (5, 35000), (6, 45000)],
    103: [(7, 22000), (8, 27000), (9, 26000)]
}
for dept,employee in data.items():
    salarys=[]
    for emp in employee:
        salarys.append(emp[1])
    print("Department:", dept)
    print("Minimum Salary:", min(salarys))
    print("Maximum Salary:", max(salarys))
