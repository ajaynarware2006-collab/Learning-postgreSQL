import psycopg as pg
from check_balance import check_balance
from check_user import check_user
from connecting_database import connecting
from perfrom_transaction import perfrom_transaction


cursor,connection=connecting()

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
