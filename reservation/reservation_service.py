from reservation import reservation_repository
from bson import ObjectId 

from datetime import datetime

from flask import Flask

def write_a_post(given_resv): 
    date = datetime.now()
    given_resv['rgstr_date-time'] = str(date)
    result = reservation_repository.write_resv(given_resv)
    
    if result is not None:
        return True
    else: 
        return False