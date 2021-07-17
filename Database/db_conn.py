import mysql.connector 

connection=mysql.connector.connect(host="localhost",user="root",password="2065")

# print(connection)

cur_obj=connection.cursor()

cur_obj.execute("show database")

for i in cur_obj:
    print(i)

# cur_obj.execute("create database jpya5")
# print("Database Created!!")
# connection.close()