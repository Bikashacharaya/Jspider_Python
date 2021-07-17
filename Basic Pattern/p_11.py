'''
2 4 6 8 10
12 14 16 18 20
22 24 26 28 30
32 34 36 38 40
42 44 46 48 50
'''
num = int(input("Enter any number: "))
x = 2
for row in range(1, num+1):
    for col in range(1, num+1):
        print(x, end=" ")
        x = x+2
    print()
