from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbdreamshare

def insert_all():
    doc = {
        'user_id': 'test_id',
        'user_name': 'test_name',
        'password': '8A63F2140468B05CEC054770D3267430B7FC098D2300830BBE93CED14281823B',    #testpassword123!
        'ntfct_count': 0,
    }
    return db.user.insert_one(doc)


if __name__ == '__main__':
    # 기존의 movies 콜렉션을 삭제하기
    db.movies.drop()

    # 영화 사이트를 scraping 해서 db 에 채우기
insert_all()