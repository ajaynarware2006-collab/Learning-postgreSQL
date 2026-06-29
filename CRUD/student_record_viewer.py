import psycopg as pg
from password import password
from student_details import student_details

with pg.connect(
        host="localhost",
        dbname="expense_tracker",
        user="postgres",
        password=password(),
        port=5432) as connection:
    
    with connection.cursor() as cursor:


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

                choice=input("Choose: ")
                print()

                if choice=="1": 
                    cursor.execute("SELECT * FROM student")
                    rows=cursor.fetchall()
                    if rows==[]:
                        print("The table is empty now")
                    else:
                        for row in rows:
                            student_details(row)


                elif choice=="2":
                    try:
                        id=int(input("Enter Sudent ID :"))
                        cursor.execute(f"SELECT * FROM student WHERE student_id={id}")
                        row=cursor.fetchone()
                        student_details(row)

                    except Exception as e:
                        print(e)
                
                elif choice=="3":
                    age=int(input("Enter minimum Age :"))
                    cursor.execute(f"SELECT * FROM student WHERE age >{age}")
                    rows=cursor.fetchall()
                    if rows==[]:
                        print(f"There is no student is older then {age}")
                    else:
                        for row in rows:
                            student_details(row)

                elif choice=="4":
                    cursor.execute("SELECT COUNT(*) FROM student")
                    count=cursor.fetchall()

                    print(f"Count is {count[0][0]}")

                elif choice=="5":
                    break

                else:
                    print("PLEASE Enter valid input")

        except Exception as e:
            print(e)

        finally:
            cursor.close()
            connection.close()