import psycopg as pg
from password import password

try:
    conn =pg.connect(
        host="localhost",
        dbname="expense_tracker",
        user="postgres",
        password=password(),
        port=5432
    )

    cursor=conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows=cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print(e)

finally:
    cursor.close()
    conn.close()
    