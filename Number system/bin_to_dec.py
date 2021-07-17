# binary to decimal conversion

bin = int(input("Enter any number: "))
temp = bin
pow = 0
sum = 0
while(bin != 0):
    ext = bin % 10
    mul = ext*(2**pow)
    sum = sum+mul
    bin = bin//10
    pow += 1
print(f"The conversion of Binary number {temp} to decimal is {sum}")
