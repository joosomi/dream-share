from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbdreamshare

def register(user):
    doc = {
        'user_id': user['id_receive'],
        'user_name': user['user_name_receive'],
        'password': user['pw_receive'],
        'ntfct_count': 0,
    }
    return db.user.insert_one(doc)