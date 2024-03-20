from board import board_repository
from bson import ObjectId 

#전체 게시글 가져오기 
def get_all_posts():
    posts = board_repository.get_posts()
    if posts is not None:
        return posts
    else:
        return None

#특정 게시글 가져오기
def get_a_post(post_id):
    try:
        id = ObjectId(post_id)
        post = board_repository.getpost(id)
        if post:
            post['_id'] = str(post['_id'])
            return post
        else:
            return None
    except Exception as e:
        print(e) 
        return None

#게시글 쓰기
def write_a_post(given_post): 
    result = board_repository.write_post(given_post)
    if result is not None:
        return True
    else: 
        return False


# #게시글 수정
# def edit_a_post(post):
#     post["post_id"] = (ObjectId(post["post_id"]))
    
#     edited_result = board_repository.edit_post(post)


#게시글 삭제
def delete_a_post(post_id):
    id = (ObjectId(post_id))
    deleted_count= board_repository.delete_post(id)
    
    if deleted_count>0:
        return True
    else: 
        return False