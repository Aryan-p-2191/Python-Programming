'''Calculate net sales where net sales = gross sales - 10% discount 
of gross sales.'''
gross = int(input("Enter gross:"))
discount = gross * 0.1
print(f"Net sales = {gross - discount}")