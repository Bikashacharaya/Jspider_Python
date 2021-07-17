'''
0 0 * 0 0
0 0 * 0 0
* * * * *
0 0 * 0 0
0 0 * 0 0
'''
n = int(input("Enter any input: "))

for row in range(n):
    for col in range(n):
        if row == n//2 or col == n//2:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()
