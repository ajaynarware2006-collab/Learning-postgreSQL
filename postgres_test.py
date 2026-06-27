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

    conn.close()

except Exception as e:
    print(e)
    