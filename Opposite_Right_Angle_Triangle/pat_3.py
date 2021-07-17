'''
5 4 3 2 1
5 4 3 2
5 4 3 
5 4
5 
'''
n = int(input("Enter any number: "))

for row in range(1, n+1):
    for col in range(n, row-1, -1):
        print(col, end=" ")
    print()
