'''

    1
  1 2 3
1 2 3 4 5

'''

n = int(input("Enter any number: "))
for row in range(1, n):
    for spc in range(row, n-1):
        print(" ", end=" ")
    for str in range(1, row*2):
        print(str, end=" ")
    print()
