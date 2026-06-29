from connecting_database import connecting

connection,cursor=connecting()

def check_user(account_id):
    cursor.execute("SELECT * FROM account WHERE account_id=%s",(account_id,))
    user=cursor.fetchone()
    print(user)


    if user==None:
        print()
        raise Exception("User not Exists")
    
    return
        
