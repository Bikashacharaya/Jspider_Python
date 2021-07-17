
num = int(input("Enter any number: "))
for row in range(1, num+1):
    for col in range(num, row-1, -1):
        print(row, end=" ")
    print()
