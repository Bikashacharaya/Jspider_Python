# output: 5 10 20 40 80 160
num = int(input("Enter any value: "))
x = 5
for i in range(1, num+1):
    print(x, end=" ")
    x = x*2
