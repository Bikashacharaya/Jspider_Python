'''
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
'''
num = int(input("Enter any number: "))

for row in range(1, num+1):
    for col in range(1, num+1):
        print(row*col, end=" ")
    print()
