import psycopg as pg
from password import password

conn =pg.connect(
        host="localhost",
        dbname="expense_tracker",
        user="postgres",
        password=password(),
        port=5432
        )

cursor=conn.cursor()

while True:
        print("===========================")
        print()
        print("Press 1 to insert data")
        print("Press 2 to view data")
        print("Press 3 to exit")
        print()
        choice=input("Enter your choice :")
        if choice=="1":
                name=input("Name : ")
                age=int(input("Age  :"))
                cursor.execute("INSERT INTO student(name , age) VALUES(%s,%s)",(name,age))
        
        elif choice=="2":
                cursor.execute("SELECT * FROM student")


conn.commit()
data=cursor.fetchall()
print(data)

cursor.close()
conn.close()