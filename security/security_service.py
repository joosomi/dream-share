import datetime
from dotenv import load_dotenv
import os
import jwt

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")

def issueToken(id_receive):
        payload = {
            'id': id_receive,
            'exp':  datetime.datetime.utcnow() + datetime.timedelta(seconds=1800)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token