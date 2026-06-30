from password import password
import psycopg as pg

with pg.connect(
            host="localhost",
            dbname="school_mangement",
            user="postgres",
            password=password(),
            port=5432) as connection:
        
        with connection.cursor() as cursor:
                # cursor.execute("CREATE VIEW student_info AS SELECT name , age FROM student")

                # connection.commit()
                # print("View Created")

                cursor.execute("SELECT * FROM student_info")

                data=cursor.fetchall()
                print(f"{'Name':<15} {'Age'}")
                for student in data:
                        print("----------------------")
                        print(f"{student[0]:<15}{student[1]}")