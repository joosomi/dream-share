from reservation import reservation_repository
from board import board_service
from bson import ObjectId 

from datetime import datetime

from flask import Flask

def write_a_resv(given_resv): 
    date = datetime.now()
    given_resv['rgstr_date_time'] = str(date)
    result = reservation_repository.write_resv(given_resv)
    if result is not None:
        return True
    else: 
        return False

def get_reservation_list(board_id):
    result = reservation_repository.get_resv_list_by_board_id(board_id)
    if result is not None:
        return result
    else:
        return None

def pick_resv(resv_id):
    id = ObjectId(resv_id)
    picked_resv = reservation_repository.find_one_by_id(id)
    post_id = picked_resv['post_id']
    unpicked_resv = reservation_repository.get_resv_list_by_board_id(post_id)
    reservation_repository.flag_fail(unpicked_resv)
    result =  reservation_repository.flag_success(picked_resv)

    if (result.modified_count == 1):
        board_service.change_status_to_2(post_id)
        return True
    else:
        return False