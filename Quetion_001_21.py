'''Calculate net salary 
	where net salary = gross salary + allowance - deduction.
	Allowances are 10% while deductions are 3% of gross salary.
'''
gross = int(input("Enter gross salary:"))
allowance=gross*0.1
deduction=gross*0.03
print(F"net salary = {gross + allowance - deduction}")