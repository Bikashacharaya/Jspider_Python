# FIND THE EVEN ELEMENT IN LIST AND ITS SUM
lst = [1, 3, 9, 11, 60, 71, 100, 199, 150, 300, 600, 90]
sum_even = 0
for i in lst:
    if i % 2 == 0:
        print(f"The even element are : {i} ")
        sum_even += i

print(f"The sum of even element is: {sum_even} ")
