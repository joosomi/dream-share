from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbdreamshare

def write_resv(resv):
    return db.reservation.insert_one(resv)

def get_resv_list_by_board_id(board_id):
    reservations = list(db.reservation.find({'post_id' : board_id}))
    for reservation in reservations:
        reservation['_id'] = str(reservation['_id'])
        reservation['user_id'] = str(reservation['user_id'])
    return reservations