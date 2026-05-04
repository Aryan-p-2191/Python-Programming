'''A website records visitor IDs for two different days as sets.
Write a program to:
01.Find visitors who visited both days.
02.Find visitors who visited only one of the days.
03.Find total unique visitors across both days.''' 

day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}
print(f"visitors who visited both days.:{day1&day2}")
print(f'visitors who visited only one of the days.:{(day1|day2)-(day1&day2)}')
print(F"total unique visitors across both days.:{day2|day1}")