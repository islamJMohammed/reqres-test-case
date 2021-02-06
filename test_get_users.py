#import part
import pprint
import pytest

##################users Branch
from jsonpath import jsonpath

import json

from user_services import *
from helper import *



def test_get_users_list():
    excepted_status_code=200
    print("\nThe test_get_users_list start")
    response=get_users_list()
    print("\nThe response have been return")
    json_text=json.loads(response.text)
    data=jsonpath(json_text,'data')
    expected_user_count=len(store_user_info(data[0]))
    real_user_count=jsonpath(json_text,'per_page')[0]
    print("\nThe expected number of users is "+str(expected_user_count))
    print("\nThe real number of users is " + str(real_user_count))
    assert real_user_count == expected_user_count
    print("\nThe expected status code is "+str(excepted_status_code))
    print("\nThe real status code is " + str(response.status_code))
    assert response.status_code==excepted_status_code
    print("\nThe test_get_users_list over")

def test_get_single_user():
    user_id=2
    excepted_status_code = 200
    print("\nThe test_get_single_user start")
    response=get_single_user(user_id)
    print("\nThe response have been return")
    json_text = json.loads(response.text)
    data = jsonpath(json_text, 'data')
    print data[0]
    print("\nThe expected status code is "+str(excepted_status_code))
    print("\nThe real status code is " + str(response.status_code))
    assert response.status_code == excepted_status_code
    print("\nThe test_get_single_user over")


def test_get_single_user_not_found():
    user_id=23
    excepted_status_code = 404
    print("\nThe test_get_single_user_not_found start")
    response=get_single_user_not_found(user_id)
    print("\nThe expected status code is "+str(excepted_status_code))
    print("\nThe real status code is " + str(response.status_code))
    assert response.status_code == excepted_status_code
    print("\nThe test_get_single_user_not_found over")
