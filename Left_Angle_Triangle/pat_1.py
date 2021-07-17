'''
        1 
      2 2 
    3 3 3 
  4 4 4 4
5 5 5 5 5

'''

n = int(input("Enter any number: "))

for row in range(1, n+1):
    for spc in range(n, row, -1):
        print(" ", end=" ")
    for str in range(row):
        print(row, end=" ")
    print()
