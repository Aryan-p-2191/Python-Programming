'''Convert list of temperatures in Fahrenheit degrees to equivalent 
Celsius degrees.'''

F = [32, 68, 77, 104, 50]

print("Temperatures in Fahrenheit:")
print(F)


C = []

for x in F:
    celsius = (x - 32) * 5/9
    C.append(celsius)

print("\nTemperatures in Celsius:")
print(C)