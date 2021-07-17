import mysql.connector

con_obj=mysql.connector.connect(host="localhost",user="root",password="2065")

print(con_obj)

cur_ob=con_obj.cursor()

try:
    cur_ob.execute("show database")

except:
    con_obj.rollback()


for x in cur_ob:
    print(x)

con_obj.close()

