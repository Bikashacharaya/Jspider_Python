'''
      *
    * * *
  * * * * *
* * * * * * *

'''

n = int(input("Enter any number: "))

for row in range(1, n):
    for spc in range(row, n-1):
        print(" ", end=" ")
    for str in range(1, row*2):
        print("*", end=" ")
    print()
