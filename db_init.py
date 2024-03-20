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
        'owner_id': 'test_id',
        'status': 0
    }
    return db.board.insert_one(post)

def insert_reservation():
    post = {
        'user_id': 'test_id',
        'post_id': '65fa8d2007afa26f216ca718',
        'contact-information': '010-0000-0000',
        'status': 1,
        'rgstr_date_time': '2025-07-23 00:00:00',
    }
    return db.reservation.insert_one(post)
if __name__ == '__main__':
    db.user.drop()
    db.board.drop()
    db.reservation.drop()

insert_all()
insert_board()
insert_reservation()