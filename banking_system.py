import psycopg as pg
from password import password

connection=pg.connect(
    host="localhost",
    dbname="banking_system",
    user="postgres",
    password=password(),
    port=5432
)

cursor=connection.cursor()

try:
    sender=int(input("Enter Sender's account ID : "))
    amount=int(input("Enter amount to send : "))
    reciver=int(input("Enter reciver's account ID : "))
    print()
    cursor.execute("UPDATE account SET amount=amount-%s WHERE account_id=%s",(amount,sender))

    cursor.execute("UPDATE account SET amount=amount+%s WHERE account_id=%s",(amount,reciver))

    connection.commit()
    print("Money Transfer seccessfully")

except Exception as e:
    connection.rollback()
    print(e)


cursor.execute("SELECT * FROM account ORDER BY account_id")
data=cursor.fetchall()
for account in data:
    print("=============================")
    print(f"Name       : {account[1]}")
    print(f"Amount     : {account[2]}")
    print(f"Account ID : {account[0]}")
    print("=============================")

