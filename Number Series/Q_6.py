# output: 3 2 9 4 15 6 21 8 27

num = int(input("Enter any value: "))

for i in range(1, num+1):
    if(i % 2 == 0):
        print(i, end=" ")
    else:
        print(i*3, end=" ")
