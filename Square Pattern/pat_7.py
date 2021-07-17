'''
        *
        *
        *
        *
* * * * *     
'''
n = int(input("Enter any input: "))

for row in range(1, n+1):
    for col in range(1, n+1):
        if row == n+1//2 or col == n+1//2:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()
