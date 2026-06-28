import psycopg as pg
from password import password


def connecting():
    conn =pg.connect(
        host="localhost",
        dbname="expense_tracker",
        user="postgres",
        password=password(),
        port=5432)
    cursor=conn.cursor()
    return conn,cursor