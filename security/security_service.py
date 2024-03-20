import datetime
from dotenv import load_dotenv
import os
import jwt
from user import user_repository

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")

def issueToken(id_receive):
        payload = {
            'id': id_receive,
            'exp':  datetime.datetime.utcnow() + datetime.timedelta(seconds=1800)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token

def getIdWithValidation(receive_token):
    try:
        payload = jwt.decode(receive_token, SECRET_KEY, algorithms=['HS256'])
        userinfo = user_repository.find_one_by_id(payload['id'])
        return {"result": True, "id": userinfo['_id']}

    except jwt.ExpiredSignatureError:
        return  {"result": False, "msg":"로그인 시간이 만료되었습니다."}
    except jwt.exceptions.DecodeError:
        return  {"result": False, "msg":"로그인 정보가 존재하지 않습니다."}

def validateToken(receive_token):
    try:
        payload = jwt.decode(receive_token, SECRET_KEY, algorithms=['HS256'])
        userinfo = user_repository.find_one_by_id(payload['id'])
        return {"result": True, "data": userinfo['user_id']}

    except jwt.ExpiredSignatureError:
        return  {"result": False, "msg":"로그인 시간이 만료되었습니다."}
    except jwt.exceptions.DecodeError:
        return  {"result": False, "msg":"로그인 정보가 존재하지 않습니다."}