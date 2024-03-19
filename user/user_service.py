import hashlib
import user_repository

def sign_up(given_user):
    pw_receive = given_user['pw_receive']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    user = dict()
    user['id_receive'] = given_user['id_give']
    user['pw_receive'] = pw_hash
    user['username_receive'] = given_user['username_receive']

    return user_repository.register(user)