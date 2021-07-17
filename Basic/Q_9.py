# Python Program for Sum of squares of first n natural numbers

start_num = int(input("Enter the starting value: "))
end_num = int(input("Enter the ending value: "))
sum = 0
for i in range(start_num, end_num):
    sqr = i*i
    sum = sum+sqr
print(f"The sum of square between {start_num} & {end_num} is {sum}")
