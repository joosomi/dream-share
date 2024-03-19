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


if __name__ == '__main__':
    # 기존의 movies 콜렉션을 삭제하기
    db.user.drop()

    # 영화 사이트를 scraping 해서 db 에 채우기
insert_all()