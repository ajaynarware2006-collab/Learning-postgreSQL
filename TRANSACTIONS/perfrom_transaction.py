from connecting_database import connecting

connection,cursor=connecting()

def perfrom_transaction(amount,sender,reciver):
    cursor.execute("UPDATE account SET amount=amount-%s WHERE account_id=%s",(amount,sender))

    cursor.execute("UPDATE account SET amount=amount+%s WHERE account_id=%s",(amount,reciver))

    connection.commit()
    print("Money Transfer seccessfully")