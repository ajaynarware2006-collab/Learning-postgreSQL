from connecting_database import connecting

connection,cursor=connecting()

def check_balance(amount,account_id):
    cursor.execute("SELECT * FROM account WHERE account_id=%s",(account_id,))
    sender=cursor.fetchone()
    if sender[2]<amount:
        raise Exception("Inefficient Balance")