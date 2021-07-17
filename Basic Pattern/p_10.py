'''
1 3 5 7 9
11 13 15 17 19
21 23 25 27 29
31 33 35 37 39
41 43 45 47 49
'''
num = int(input("Enter any number: "))
x = 1
for row in range(1, num+1):
    for col in range(1, num+1):
        print(x, end=" ")
        x = x+2
    print()
