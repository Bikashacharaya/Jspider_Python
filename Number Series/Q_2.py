# output: 1 4 7 10 13 16 19

num = int(input("Enter any value: "))
x = 1
dif = 3

for i in range(1, num+1):
    print(x, end=" ")
    x = x+dif
