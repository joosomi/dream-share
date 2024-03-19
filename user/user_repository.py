from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbdreamshare

def register(user):
    doc = {
        'user_id': user['id_receive'],
        'username': user['username_receive'],
        'password': user['pw_receive'],
        'ntfct_count': 0,
    }
    return db.user.insert_one(doc)

def usernameIsExist(username):
    return db.user.find_one({'username': username})

def userIdIsExist(user_id):
    return db.user.find_one({'user_id': user_id})