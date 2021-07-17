'''
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''
num = int(input("Enter any number: "))
for row in range(1, num+1):
    for col in range(1, num+1):
        print(chr(row+64), end=" ")
    print()
