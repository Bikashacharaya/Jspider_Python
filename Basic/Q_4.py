# Python Program for simple interest

pric = int(input("Enter the pricipal: "))
time = int(input("Enter the time: "))
rate = int(input("Enter the rate: "))

SI = (pric*time*rate)/100

print(f"The SI of pricipal:{pric}, time: {time} & rate:{rate} is :{SI}")
