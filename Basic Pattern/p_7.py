'''
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
'''
num = int(input("Enter any number: "))
for row in range(1, num+1):
    for col in range(1, num+1):
        print(chr(col+64), end=" ")
    print()
