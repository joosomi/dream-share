from pymongo import MongoClient
import hashlib
client = MongoClient('localhost', 27017)
db = client.dbdreamshare

def insert_all():
    pw = 'testpassword123!'
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    doc = {
        'user_id': 'test_id',
        'username': 'test_name',
        'password': pw_hash,    #testpassword123!
        'ntfct_count': 0,
    }
    return db.user.insert_one(doc)

def insert_board():
    post = {
        'owner_id': 'hello',
        'category': 0,
        'content': 'hi',
        'location':'dorm',
        'user_id': 'test_id',
        'status': 0
    }
    return db.board.insert_one(post)

if __name__ == '__main__':
    db.user.drop()

insert_all()
insert_board()