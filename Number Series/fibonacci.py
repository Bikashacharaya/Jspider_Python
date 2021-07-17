num = int(input("Enter any  number: "))
n1 = 0
n2 = 1
print(n1, end=" ")
print(n2, end=" ")
for i in range(2, num):
    r = n1+n2
    n1 = n2
    n2 = r
    print(r, end=" ")
