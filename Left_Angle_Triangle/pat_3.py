'''
        5 
      4 4 
    3 3 3 
  2 2 2 2 
1 1 1 1 1 

'''

n = int(input("Enter any number: "))

for row in range(1, n+1):
    for spc in range(n, row, -1):
        print(" ", end=" ")
    for val in range(row, 0, -1):
        print(n+1 - row, end=" ")
    print()
