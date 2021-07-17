import random
bank_detail = [{
    'id': '1001',
    'name': "Bikash Acharaya",
    'phn_num': 9606223683,
    'email': 'bik@gmail.com',
    'add': 'Bangalore',
    'branch': 'Bangalore',
    'acc_type': 'saving',
    'tot_amt': 50000
}]


def view():
    for detail in bank_detail:
        for key, value in detail.items():
            print(key, "->", value)
        print("-"*45)


def register():
    account_num = random.randint(11111, 99999)
    name = input("Enter Account Holder Name: ")
    contact = input("Enter Account Holder Contact Number: ")
    email_add = input("Enter Account Holder Email: ")
    address = input("Enter Account Holder Address:  ")
    branch_name = input("Enter Bank Branch: ")
    type = input("Enter Account Type : ")
    amount = int(input("Enter Amount to Deposite: "))

    bank_detail.append({'id': account_num, 'name': name, 'phn_num': contact,
                        'email': email_add, 'add': address, 'branch': branch_name, 'acc_type': type, 'tot_amt': amount})
    print("---Account Register Sucessfull--")


def search():
    acc_num = input("Enter Account Number: ")
    for detail in bank_detail:
        if (detail['id'] == acc_num):
            print(detail)
        else:
            print("---Please Enter Valid Account Number---")


def deposite():
    acc_num = input("Enter Account Number: ")
    for detail in bank_detail:
        if(detail['id'] == acc_num):
            depo_amt = int(input("Enter Deposite Amount: "))
            detail['tot_amt'] += depo_amt
            print('--Amount Deposite Sucessfully--')
            print(f"---Reamining Balance is {detail['tot_amt']}---")
        else:
            print("---Please Enter Valid Account Number--- ")


def withdraw():
    acc_num = input("Enter Account Number: ")
    for detail in bank_detail:
        if(detail['id'] == acc_num):
            wid_amt = int(input("Enter Withdraw Amount: "))
            if (detail['tot_amt'] > wid_amt):
                detail['tot_amt'] -= wid_amt
                print('--Amount Withdraw Sucessfull--')
                print(f"---Reamining Balance is {detail['tot_amt']}---")
            else:
                print("--Insuffient Banlace--")
        else:
            print("---Please Enter Valid Account Number---")


def delete_acc():
    acc_num = input("Enter the Employee ID: ")
    for detail in bank_detail:
        if(detail["id"] == acc_num):
            index = bank_detail.index(detail)
            del bank_detail[index]
            print("---The Account deleted Sucessfully---")

        else:
            print("---Account Number incorrect---")


def quit():
    print('---THANKYOU FOR VISITING US---')
