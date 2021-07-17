# Python Program for cube sum of first n natural numbers

start_num = int(input("Enter the starting value: "))
end_num = int(input("Enter the ending value: "))
sum = 0
for i in range(start_num, end_num):
    cube = i*i*i
    sum = sum+cube
print(f"The sum of cube between {start_num} & {end_num} is {sum}")
