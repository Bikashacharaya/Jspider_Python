bank = [
    {
        "id": "NSBI1001",
        "name": "Bikash",
        "phnum": 9606223683,
        "email": "bikashacharaya10@gmail.com",
        "deign": "Manager",
        "sal": 35000,
        "add": "Butwal Nepal"
    },
    {
        "id": "NSBI1002",
        "name": "Roojena",
        "phnum": 9606443128,
        "email": "roojenasharma05@gmail.com",
        "deign": "Cashier",
        "sal": 2500,
        "add": "Koholpur Nepal"
    }
]

while(True):
    print("--- WELCOME TO DEVELOPMENT BANK -----")
    print("Enter '1': View All Detail ")
    print("Enter '2': Search Employee Detail ")
    print("Enter '3': Update the Employee Salary")
    print("Enter '4': Delete the Employee Detail")
    print("Enter '5': Exit ")

    choice = int(input("Enter your choice: "))

    if(choice == 1):
        for emp in bank:
            for(key, value) in emp.items():
                print(key, "->", value)
            print("---------------------------")

    elif(choice == 2):
        for empid in bank:
            user = input("Enter the Employee ID: ")
            if(empid["id"] == user):
                for(key, value) in empid.items():
                    print(key, "->", value)
                print("------------------------")
        else:
            print("Please Enter valid Employee  ID")

    elif(choice == 3):
        user = input("Enter the Employee ID: ")
        update_Sal = float(input(f"Enter the updated Salary of {user}: "))
        for empid in bank:
            if(empid["id"] == user):
                empid["sal"] = update_Sal
                print("The Salary is Updated ... ")
                print("-------------------------")
            # else:
            #     print("Please, Enter the valid Employee ID")

    elif(choice == 4):
        user = input("Enter the Employee ID: ")
        for empid in bank:
            if(empid["id"] == user):
                index = bank.index(empid)
                del bank[index]
                print("The data is deleted Sucessfully !! ")
                print("-----------------------------")

    elif(choice == 5):
        print("Thanks for visiting us !!")
        print("---------------------------")
        exit()
        break

    else:
        print("Please, Enter the Valid Input !! ")
