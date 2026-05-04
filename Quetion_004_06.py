'''Print 24 hours of day with suitable suffixes like AM, PM,
 Noon and Midnight.'''

for h in range(0,24):
    if h==0:
        print("Midnight")
    elif h==12:
        print("Noon")
    elif 1<= h <= 11:
        print("AM")
    else:
        print("PM")  



