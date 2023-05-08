# sears .py

# define variable

sears_height = 442
thickness_dolarbill = 0.11 / 1000 # 0.11 in mm
num_bills = 1
day = 1

while num_bills * thickness_dolarbill < sears_height:
    print(day, num_bills, num_bills * thickness_dolarbill)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * thickness_dolarbill)
