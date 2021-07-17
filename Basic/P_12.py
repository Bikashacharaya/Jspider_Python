year = int(input("Enter any year: "))

if(year/4):
    if(year/400):
        print("It is a leap year")
    elif(year/100):
        print("It is a not leap year")
