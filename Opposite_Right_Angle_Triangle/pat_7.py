'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1 
1  
'''
n = int(input("Enter any number: "))

for row in range(n, 0, -1):
    for col in range(row, 0, -1):
        print(chr(col+64), end=" ")
    print()
