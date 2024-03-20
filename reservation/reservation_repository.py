from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbdreamshare

def write_resv(resv):
    return db.board.insert_one(resv)