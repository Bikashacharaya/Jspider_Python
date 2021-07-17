'''
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
'''
num = int(input("Enter any number: "))
for row in range(num, 0, -1):
    for col in range(num, 0, -1):
        print(row, end=" ")
    print()
