'''
5
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 

'''

n = int(input("Enter any number: "))

for row in range(n, 0, -1):
    for col in range(n, row-1, -1):
        print(col, end=" ")
    print()
