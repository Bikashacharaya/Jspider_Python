'''
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15 
16 17 18 19 20
21 22 23 24 25
'''
num = int(input("Enter any number: "))
x = 1
for row in range(1, num+1):
    for col in range(1, num+1):
        print(x, end=" ")
        x = x+1
    print()
