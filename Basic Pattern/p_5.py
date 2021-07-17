'''
5 4 3 2 1 
5 4 3 2 1
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1
'''
num = int(input("Enter any number: "))
for row in range(num, 0, -1):
    for col in range(num, 0, -1):
        print(col, end=" ")
    print()
