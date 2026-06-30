import psycopg as pg
from password import password
from student_details import student_details

with pg.connect(
        host="localhost",
        dbname="school_mangement",
        user="postgres",
        password=password(),
        port=5432) as connection:
        
        with connection.cursor() as cursor:
                
                def view_data():
                        cursor.execute("SELECT * FROM student")
                        data=cursor.fetchall()
                        return data

                def insert_data():
                        name=input("Enter Name : ")
                        age=int(input("Enter Age  : "))
                        cursor.execute("INSERT INTO student(name , age) VALUES(%s,%s)",(name,age))
                        connection.commit()
                        print("Data Inserted successfully.")


                def update_data():
                        data=view_data()
                        student_id=int(input("Enter Student id whom you want to update : "))

                        found=False
                        for student in data:
                                if student[0]==student_id:
                                        found=True
                                        new_name=input("Enter New Name : ")
                                        new_age=int(input("Enter New Age  : "))
                                        cursor.execute("UPDATE student SET name=%s , age=%s WHERE student_id=%s" , (new_name , new_age , student_id))
                                        connection.commit()
                                        print("Student Updated Successfully.")

                        if not found:
                                print("Student not found")


                def delete_data():
                        try:
                                student_id=int(input("Enter student ID you want to delete : "))
                                data=view_data()
                                found=False
                                for student in data:
                                        if student[0]==student_id:
                                                found=True
                                                final_ask=input("Are you sure? (Y/N)")
                                                if final_ask.upper()!= "Y":
                                                        print("Operation Cancelled.")

                                                else:
                                                        cursor.execute("DELETE FROM student WHERE student_id=%s",(student_id,))
                                                        connection.commit()
                                                        print("Student Deleted Successfully.")
                                                        
                                if not found:
                                        print("Student not found.")
                        except ValueError:
                                print("Enter number in student_id")

                try:
                        while True:

                                print("===========================")
                                print()
                                print("Press 1 to insert data")
                                print("Press 2 to view data")
                                print("Press 3 to update data")
                                print("Press 4 to delete data")
                                print("Press 5 to exit")
                                print()

                                choice=input("Enter your choice :")

                                if choice=="1":
                                        insert_data()

                                
                                elif choice=="2":
                                        data=view_data()
                                        if data==[]:
                                                print("There is no student data")
                                        else:
                                                for row in data:
                                                        student_details(row)
                                        

                                elif choice=="3":
                                        update_data()
                                                

                                elif choice=="4":
                                        delete_data()


                                elif choice=="5":
                                        break


                                else:
                                        print("PLEASE Enter the valid input")


                except Exception as e:
                        print(e)


                finally:
                        cursor.close()
                        connection.close()