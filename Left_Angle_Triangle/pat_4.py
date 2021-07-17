'''
        5 
      4 5 
    3 4 5 
  2 3 4 5
1 2 3 4 5

'''

n = int(input("Enter any number: "))

for row in range(1, n+1):
    for spc in range(n, row, -1):
        print(" ", end=" ")
    for val in range(row, 0, -1):
        print(n+1 - val, end=" ")
    print()
