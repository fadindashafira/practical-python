# bounce.py
#
# Exercise 1.5
height = 100 
bounce = 3/5
num_bounces = 1

while num_bounces < 11:
    height = bounce * height
    print(num_bounces, height)
    num_bounces = num_bounces + 1
    