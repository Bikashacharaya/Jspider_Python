'''

   1   
  2 3 4 
5 6 7 8 9

'''

n = int(input("Enter any number: "))
x = 1
for row in range(1, n):
    for spc in range(row, n-1):
        print(" ", end=" ")
    for str in range(1, row*2):
        print(x, end=" ")
        x = x+1
    print()
