# output: 1 4 3 8 5 12 7 16 9

num = int(input("Enter any value: "))

for i in range(1, num+1):
    if(i % 2 == 0):
        print(i*2, end=" ")
    else:
        print(i, end=" ")
