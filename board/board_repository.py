from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbdreamshare

#전체 게시글 가져오기
def get_posts():
    posts = list(db.board.find())
    for post in posts:
        post['_id'] = str(post['_id'])

    return posts

#특정 게시글 가져오기 
def getpost(post_id):
    post = db.board.find_one({'_id': post_id})
    return post

#게시글 작성
def write_post(post):
    return db.board.insert_one(post)


#게시글 수정
# def edit_post(post):    
#     post = db.board.update_one({'_id': post["post_id"], 'status':})


    
#게시글 삭제
def delete_post(post_id):
    result = db.board.delete_one({'_id': post_id})
    return result.deleted_count

def update_status_1(post_id):
    result = db.board.update_one({'_id' : post_id}, {'$set' : {'status' : '1'}})
    return
