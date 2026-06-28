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
def view_data():
        cursor.execute("SELECT * FROM student")
        data=cursor.fetchall()
        return data


try:
        while True:

                print("===========================")
                print()
                print("Press 1 to insert data")
                print("Press 2 to view data")
                print("Press 3 to update data")
                print("Press 4 to exit")
                print()

                choice=input("Enter your choice :")

                if choice=="1":
                        name=input("Enter Name : ")
                        age=int(input("Enter Age  : "))
                        cursor.execute("INSERT INTO student(name , age) VALUES(%s,%s)",(name,age))
                        conn.commit()
                        print("Data Inserted successfully")
                
                elif choice=="2":
                        data=view_data()
                        for student in data:
                                student_details(student)

                elif choice=="3":
                        data=view_data()
                        student_id=int(input("Enter Student id whom you want to update : "))

                        found=False
                        for student in data:
                                if student[0]==student_id:
                                        found=True
                                        new_name=input("Enter New Name : ")
                                        new_age=int(input("Enter New Age  : "))
                                        cursor.execute("UPDATE student SET name=%s , age=%s WHERE student_id=%s" , (new_name , new_age , student_id))
                                        conn.commit()
                                        print("Student Updated Successfully")
                                        break

                        if not found:
                                print("Student not found")
                                
                
                elif choice=="4":
                        break

                else:
                        print("PLEASE Enter the valid input")
except Exception as e:
        print(e)


finally:
        cursor.close()
        conn.close()