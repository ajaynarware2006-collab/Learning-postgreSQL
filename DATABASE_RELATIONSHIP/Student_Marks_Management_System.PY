import psycopg as pg
from password import password

def insert_student():
    name=input("Enter student's name : ")
    cursor.execute("INSERT INTO students(name) VALUES(%s) RETURNING student_id",(name,))
    student_id=cursor.fetchone()[0]
    print(f"Student ID fro student {name} is {student_id}")

def add_marks():
    student_id=int(input("Enter Student id : "))
    subject=input("Enter subject name : ")
    marks=int(input("Enter Student marks : "))

    cursor.execute("INSERT INTO marks(subject,marks,student_id) VALUES(%s,%s,%s)",(subject,marks,student_id))

def view_students():
    cursor.execute("SELECT * FROM students ORDER BY student_id")
    data=cursor.fetchall()
    print("Student ID      Name ")
    for student in data:
        print("------------------------------------------")
        print(f"     {student[0]}          {student[1]}")

def view_marks():
    student_id=int(input("Enter Student id : "))
    cursor.execute("SELECT * FROM marks WHERE student_id=%s",(student_id,))
    data=cursor.fetchall()

    cursor.execute("SELECT * FROM students WHERE student_id=%s",(student_id,))
    name=cursor.fetchone()[1]
    print(f"Name --> {name}")
    for student in data:
        print(f"{student[1]} -> {student[2]}")

operation={
    "1":insert_student,
    "2":add_marks,
    "3":view_students,
    "4":view_marks
}

try:
    with pg.connect(
            host="localhost",
            dbname="school_mangement",
            user="postgres",
            password=password(),
            port=5432) as connection:
        
        with connection.cursor() as cursor:
            while True:

                print("==============================")
                print("1. Add Student")
                print("2. Add Marks")
                print("3. View Students")
                print("4. View Student Marks")
                print("5. Exit")
                print()

                choice=input("Enter your choice : ")
                print()
                if choice=="5":
                    break
                else:
                    try:
                        runnung_task=operation[choice]()
                    
                    except KeyError:
                        print("Please Enter Valid input")

except Exception as e:
    print("ERROR :",e)
