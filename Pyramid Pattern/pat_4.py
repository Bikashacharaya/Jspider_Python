'''
* * * * *
  * * *
    *
'''
n = int(input("Enter any number: "))

for row in range(n-1, 0, -1):
    for spc in range(1, n-row):
        print(" ", end=" ")
    for str in range(1, 2*row):
        print("*", end=" ")

    print()
