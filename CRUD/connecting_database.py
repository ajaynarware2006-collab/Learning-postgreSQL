import psycopg as pg
from password import password


def connecting():
    conn =pg.connect(
        host="localhost",
        dbname="school_mangement",
        user="postgres",
        password=password(),
        port=5432)
    cursor=conn.cursor()
    return conn,cursor