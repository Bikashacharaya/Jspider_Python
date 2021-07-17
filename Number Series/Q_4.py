# output: 2 1 4 3 6 5 8 7 10

num = int(input("Enter any value: "))

for i in range(1, num+1):
    if(i % 2 == 0):
        print(i-1, end=" ")
    else:
        print(i+1, end=" ")
