# Bank application
# This code Written-by @Bikash
import random
bank = [{
    "acc_num": "1001",
    "acc_name": "Bikash Acharaya",
    "phn_num": +919606223683,
    "email": "bikashacharaya10@gmail.com",
    "add": "Bangalore",
    "branch": "Sahakarnagar Bangalore ",
    "tot_amt": 50000
}]


while(True):

    # Display on front
    print()
    print("---WELCOME TO DEVELOPMENT BANK---")
    print("Enter-'1' View Detail of Account Holder ")
    print("Enter-'2' New Register Account")
    print("Enter-'3' Serach for Account Holder ")
    print("Enter-'4' Deposite Money")
    print("Enter-'5' Withdraw Money")
    print("Enter-'6' Delete Account")
    print("Enter-'7' Quit")
    print()

    # choice from user

    ch = int(input("Enter your choice: "))

    # Detail of Account Holder
    if(ch == 1):
        for detail in bank:
            for key, value in detail.items():
                print(key, " : ", value)
            print("------------------------------")

    # New Register Account
    if(ch == 2):

        account_num = random.randint(11111, 99999)
        name = input("Enter Account Holder Name: ")
        contact = input("Enter Account Holder Contact Number: ")
        email_add = input("Enter Account Holder Email: ")
        address = input("Enter Account Holder Address:  ")
        branch_name = input("Enter Bank Branch: ")
        type = input("Enter Account Type : ")
        amount = int(input("Enter Amount to Deposite: "))

        bank.append({'acc_num': account_num, 'acc_name': name, 'phn_num': contact,
                     'email': email_add, 'add': address, 'branch': branch_name, 'tot_amt': amount})
        print("---Account Register Sucessfull--")

    # Search Account Number
    elif (ch == 3):
        acc_id = input("Enter Account Number: ")
        for acc in bank:
            if(acc["acc_num"] == acc_id):
                for key, value in acc.items():
                    print(key, " : ", value)
                print("--------------------------")
            else:
                print("----------------------------")
                print("Account Number incorrect !")
                print("----------------------------")

    # Deposite Amount
    elif(ch == 4):
        acc_id = input("Enter Account Number: ")

        for acc in bank:
            if(acc["acc_num"] == acc_id):
                depo_amt = int(input("Enter Deposite Amount: "))
                acc["tot_amt"] += depo_amt
                print("----------------------------")
                print("Amount Deposite Sucessfull !")
                print("----------------------------")
            else:
                print("---------------------------")
                print("Account Number incorrect !")
                print("----------------------------")

    # Withdraw Amount
    elif(ch == 5):
        acc_id = input("Enter Account Number: ")

        for acc in bank:
            if(acc["acc_num"] == acc_id):
                withdraw_amt = int(input("Enter Withdraw Amount: "))
                if(acc["tot_amt"] < withdraw_amt):
                    print("------------------------")
                    print("---Insufficient Money----")
                    print("--------------------------")
                else:
                    acc["tot_amt"] -= withdraw_amt
                    print("--------------------------")
                    print("Amount Withdraw Sucessfull !")
                    print("--------------------------")

            else:
                print("--------------------------")
                print("Account Number incorrect !")
                print("---------------------------")

    # Delete Account
    elif(ch == 6):
        user = input("Enter the Employee ID: ")
        for acc in bank:
            if(acc["acc_num"] == user):
                index = bank.index(acc)
                del bank[index]
                print("-----------------------------")
                print("The Account deleted Sucessfully !! ")
                print("-----------------------------")
            else:
                print("--------------------------")
                print("Account Number incorrect !")
                print("---------------------------")

    # Quit Apllication

    elif(ch == 7):
        print("---Thankyou for Visiting Us---")
        break

    # Invalid Options
    else:
        print("--Please Enter Valid Options-----")
