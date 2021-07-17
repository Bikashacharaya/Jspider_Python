# Find the minimum value in the list
lst = [1, 3, 9, 11, 60, 71, 100, 199, 150, 300, 600, 90]
min = lst[0]
for i in lst:
    if min > i:
        min = i
print(f"The maximum value: {min}")
