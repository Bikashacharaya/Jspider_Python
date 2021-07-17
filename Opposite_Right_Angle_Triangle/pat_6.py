'''
1 2 3 4 5 
6 7 8 9
10 11 12 
13 14 
15 
'''

n = int(input("Enter any number: "))
x = 1
for row in range(n+1, 1, -1):
    for col in range(1, row):
        print(x, end=" ")
        x = x+1
    print()
