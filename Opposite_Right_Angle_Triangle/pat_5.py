'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

n = int(input("Enter any number: "))

for row in range(n, 0, -1):
    for col in range(row):
        print(row, end=" ")
    print()
