# bounce.py
#
# Exercise 1.5

height = 100  # meters

print(0, height)
for i in range(1, 11):
    height *= 3/5
    height = round(height, 4)
    print(i, height)
