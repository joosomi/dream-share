from pymongo import MongoClient
from bson import ObjectId
client = MongoClient('mongodb://test:test@3.36.87.209', 27017)
db = client.dbdreamshare

def write_resv(resv):
    return db.reservation.insert_one(resv)

def get_resv_list_by_board_id(board_id):
    reservations = list(db.reservation.find({'post_id' : board_id}))
    for reservation in reservations:
        reservation['_id'] = str(reservation['_id'])
        reservation['user_id'] = str(reservation['user_id'])
    return reservations

def find_one_by_id(resv_id):
    id = ObjectId(resv_id)
    return db.reservation.find_one({'_id' : id})

def flag_fail(unpicked_resv_list):
    for unpicked_resv in unpicked_resv_list:
        unpicked_resv_id = unpicked_resv['_id']
        id = ObjectId(unpicked_resv_id)
        db.reservation.update_one({'_id' : id}, {'$set': {'status': 1}})
    return

def flag_success(picked_resv):
    return db.reservation.update_one({'_id' : picked_resv['_id']}, {'$set': {'status': 2}})