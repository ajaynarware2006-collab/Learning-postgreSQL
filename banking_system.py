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

cursor.execute("SELECT * FROM account ORDER BY account_id")
data=cursor.fetchall()

def view_users():
    for account in data:
        print("=============================")
        print(f"Name       : {account[1]}")
        print(f"Amount     : {account[2]}")
        print(f"Account ID : {account[0]}")
        print("=============================")

def check_user(account_id):
    exists=False
    for user in data:
        if user[0]==account_id:
            exists==True
            return

    if not exists:
        print()
        raise Exception("User not Exists")
        
def check_balance(amount,account_id):
    cursor.execute("SELECT * FROM account WHERE account_id=%s",(account_id,))
    sender=cursor.fetchone()
    if sender[2]<amount:
        raise Exception("Inefficient Balance")



try:
    sender=int(input("Enter Sender's account ID : "))
    check_user(sender)

    amount=int(input("Enter amount to send : "))
    check_balance(amount,sender)

    reciver=int(input("Enter reciver's account ID : "))
    check_user(reciver)
    print()

    if sender==reciver:
        raise Exception("Sender and Reciver cannot be same")
    
    else:   
        cursor.execute("UPDATE account SET amount=amount-%s WHERE account_id=%s",(amount,sender))

        cursor.execute("UPDATE account SET amount=amount+%s WHERE account_id=%s",(amount,reciver))

        connection.commit()
        print("Money Transfer seccessfully")

except Exception as e:
    connection.rollback()
    print(e)
