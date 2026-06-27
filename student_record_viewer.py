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
try:
    while True:
        print("========= Student Record Viewer =========")
        print()
        print("Press 1 to Show all students")
        print("Press 2 to Search student by ID")
        print("Press 3 to Show students older than an age")
        print("Press 4 to Count total students")
        print("Press 5 to Exit")
        print()

        choose=input("Choose: ")
        print()

        if choose=="1": 
            cursor.execute("SELECT * FROM student")
            rows=cursor.fetchall()
            for row in rows:
                print("=========================")
                print(f"Name       : {row[1]}")
                print(f"Age        : {row[2]}")
                print(f"Student ID : {row[0]}")


        elif choose=="2":
            try:
                id=int(input("Enter Sudent ID :"))
                cursor.execute(f"SELECT * FROM student WHERE student_id={id}")
                row=cursor.fetchone()
                print("=========================")
                print(f"Name       : {row[1]}")
                print(f"Age        : {row[2]}")
                print(f"Student ID : {row[0]}")
                print("==========================")

            except Exception as e:
                print(e)
        
        elif choose=="3":
            age=int(input("Enter minimum Age :"))
            cursor.execute(f"SELECT * FROM student WHERE age >{age}")
            rows=cursor.fetchall()
            for row in rows:
                print("=========================")
                print(f"Name       : {row[1]}")
                print(f"Age        : {row[2]}")
                print(f"Student ID : {row[0]}")

        elif choose=="4":
            cursor.execute("SELECT COUNT(*) FROM student")
            count=cursor.fetchall()

            print(f"Count is {count[0][0]}")

        elif choose=="5":
            break

        else:
            print("PLEASE Enter valid input")

except Exception as e:
    print(e)

finally:
    cursor.close()
    conn.close()