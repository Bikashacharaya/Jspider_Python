'''
        1 
      1 2 
    1 2 3 
  1 2 3 4
1 2 3 4 5

'''

n = int(input("Enter any number: "))

for row in range(1, n+1):
    for spc in range(n, row, -1):
        print(" ", end=" ")
    for val in range(1, row+1):
        print(val, end=" ")
    print()
