# Ouput : 1 4 27 16 125 36 343 64

num = int(input("Enter any number: "))
x = 1
print(x, end=" ")
for i in range(2, num+1):

    if(i % 2 == 0):
        print(i**2, end=" ")
    else:
        print(i**3, end=" ")
