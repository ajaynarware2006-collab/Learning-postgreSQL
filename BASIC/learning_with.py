import psycopg as pg
from password import password

with pg.connect(
        host="localhost",
        dbname="school_mangement",
        user="postgres",
        password=password(),
        port=5432) as connection:
    
    with connection.cursor() as cursor:

        cursor.execute("SELECT * FROM student ORDER BY student_id")

        students=cursor.fetchall()

        print(students)