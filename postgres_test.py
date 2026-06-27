import psycopg as pg

try:
    conn =pg.connect(
        host="localhost",
        dbname="expense_tracker",
        user="postgres",
        password="ajaynarware",
        port=5432
    )

    print("Connected Successfully!")

    cursor=pg.cursor()
    cursor.execute("SELECT * FROM student")
    row=cursor.fetchone()
    print(row)

    conn.close()

except Exception as e:
    print(e)
    