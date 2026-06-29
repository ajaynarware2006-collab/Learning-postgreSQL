import psycopg as pg
from BACKEND_DEV.SQL.TRANSACTIONS.password import password

try:
    conn =pg.connect(
        host="localhost",
        dbname="expense_tracker",
        user="postgres",
        password=password(),
        port=5432
    )

    print("Connected Successfully!")

    conn.close()

except Exception as e:
    print(e)
    