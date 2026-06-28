import psycopg as pg
from password import password
from student_details import student_details

conn =pg.connect(
        host="localhost",
        dbname="expense_tracker",
        user="postgres",
        password=password(),
        port=5432)

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
                conn.commit()
                print("Data Inserted successfully")
        
        elif choice=="2":
                cursor.execute("SELECT * FROM student")
                data=cursor.fetchall()
                for students in data:
                        student_details(students)
        
        elif choice=="3":
                break

        else:
                print("PLEASE Enter the valid input")




cursor.close()
conn.close()