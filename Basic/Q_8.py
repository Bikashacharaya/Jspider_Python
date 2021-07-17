# Python Program to check Armstrong Number

n = int(input("Enter any number: "))
order = len(str(n))
sum = 0
copy_n = n

while(n > 0):
    digit = n % 10
    sum = sum+digit**order
    n = n//10

if (sum == copy_n):
    print(f"The {copy_n} is Arms strong number")
else:
    print(f"The {copy_n} is not a arms strong number")
