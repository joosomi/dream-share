import hashlib
from security import security_service
from user import user_repository

def sign_up(given_user):
    pw_receive = given_user['pw_receive']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    user = dict()
    user['id_receive'] = given_user['id_receive']
    user['pw_receive'] = pw_hash
    user['username_receive'] = given_user['username_receive']

    result = user_repository.register(user)
    if result is not None:
        return True
    else: 
        return False

def validateUsername(username):
    result = user_repository.usernameIsExist(username)
    if result is not None:
        return False
    else:
        return True

def validateUserId(user_id):
    result = user_repository.userIdIsExist(user_id)
    if result is not None:
        return False
    else: 
        return True

def login(given_login_form):
    id_receive = given_login_form["id_receive"]
    pw_receive = given_login_form["pw_receive"]
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    login_form = dict()

    login_form['id_receive'] = id_receive
    login_form['pw_receive'] = pw_hash
    result = user_repository.login_check(login_form)
    
    if result is not None:
        return security_service.issueToken(id_receive)
    else:
        return False