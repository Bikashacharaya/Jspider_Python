'''
    1 
  2 * 4
* 6 * 8 *

'''

n = int(input("Enter any number: "))
x = 1
for row in range(1, n):
    for spc in range(row, n-1):
        print(" ", end=" ")
    for val in range(1, row*2):
        #print(x, end=" ")
        if x % 2 == 0 or x == 1:
            print(x, end=" ")
        else:
            print("*", end=" ")
        x = x+1
    print()
