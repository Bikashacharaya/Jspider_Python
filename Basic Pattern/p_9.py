'''
A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y
'''
num = int(input("Enter any number: "))
x = 1
for row in range(1, num+1):
    for col in range(1, num+1):
        print(chr(x+64), end=" ")
        x = x+1
    print()
