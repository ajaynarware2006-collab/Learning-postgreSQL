import psycopg as pg
from password import password
from check_balance import check_balance
from check_user import check_user
from perfrom_transaction import perfrom_transaction


with pg.connect(
        host="localhost",
        dbname="banking_system",
        user="postgres",
        password=password(),
        port=5432) as connection:
    
    with connection.cursor() as cursor:

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
                perfrom_transaction(amount,sender,reciver)

        except Exception as e:
            connection.rollback()
            print(e)