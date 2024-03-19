import datetime
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


def issueToken(result):
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.date() + datetime.timedelta(seconds=1800)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')