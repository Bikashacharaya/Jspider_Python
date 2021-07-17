# Find the maxmimum value in the list
lst = [1, 3, 9, 11, 60, 71, 100, 199, 150, 300, 600, 90]
max = lst[0]
for i in lst:
    if max < i:
        max = i
        
print(f"The maximum value:{max}")
