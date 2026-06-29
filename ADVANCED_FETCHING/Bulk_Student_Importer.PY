import psycopg as pg
from password import password

with pg.connect(
        host="localhost",
        dbname="expense_tracker",
        user="postgres",
        password=password(),
        port=5432) as connection:
    
    with connection.cursor() as cursor:
        students=[]
        # while True:
        #     name=input("Enter Name : ")
        #     age=int(input("Enter age  : "))
        #     print()
        #     student=(name,age)
        #     students.append(student)
        #     choice=input("Do you wanna add another name (Y/N): ")
        #     if choice.upper()=="N":
        #          break
            
        # cursor.executemany("INSERT INTO student(name,age) VALUES(%s,%s)",students)

        # connection.commit()
        # print(f"Successfully Imported {len(students)} Students")

        cursor.execute("SELECT * FROM student ORDER BY student_id")
        print()

        total_rows=cursor.rowcount

        rows=cursor.fetchmany(5)
        print("List of 5 students are")
        for row in rows:
            print(row)

        print()
        print("Total imported students",total_rows)

        print("Using RETURNING")

        name=input("Enter Name : ")
        age=int(input("Enter age  : "))
        print()
        cursor.executemany("INSERT INTO student(name,age) VALUES(%s,%s) RETURNING student_id",[(name,age)])


