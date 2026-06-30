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
    cursor.execute("SELECT students.name,marks.subject,marks.marks FROM students INNER JOIN marks ON students.student_id = marks.student_id WHERE students.student_id =%s;",(student_id,))

    rows=cursor.fetchall()
    if not rows:
        print("NO marks found")
        return
    
    print("Name",rows[0][0])
    print()
    print("SUBJECT      MARKS")
    for row in rows:
        print(f"{row[1]}          {row[2]}")

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
                print()
                print("======Student_Marks_Management_System======")
                print()
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
