from helper import *
from user_services import *
from http_code import *

def test_create_new_user():
    excepted_status_code = HTTP_CREATED_SUCCESS
    print("\nThe test_create_new_user start")
    file_name = 'createuser.json'
    print("\nuser info in file " + file_name)
    response = create_user(file_name)
    print("\nThe expected status code is " + str(excepted_status_code))
    print("\nThe real status code is " + str(response.status_code))
    assert response.status_code == excepted_status_code
    print("\nThe test_create_new_user is over")
