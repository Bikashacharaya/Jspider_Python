'''
1 2 3 4 5 
1 2 3 4
1 2 3
1 2 
1
'''

n = int(input("Enter any number: "))

for row in range(n+1, 1, -1):
    for col in range(1, row):
        print(col, end=" ")
    print()
