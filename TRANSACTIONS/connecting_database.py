import psycopg as pg
from password import password
def connecting():
    connection=pg.connect(
        host="localhost",
        dbname="banking_system",
        user="postgres",
        password=password(),
        port=5432
    )
    cursor=connection.cursor()

    return connection,cursor

