'''
* 0 0 0 0
0 * 0 0 0
0 0 * 0 0
0 0 0 * 0
0 0 0 0 *
'''
n = int(input("Enter any input: "))

for row in range(1, n+1):
    for col in range(1, n+1):
        if row == col:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()
