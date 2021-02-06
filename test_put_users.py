from helper import *
from user_services import *

def test_update_user_info():
    excepted_status_code=201
    user_id=2
    print("\nThe test_update_user_info start")
    file_name='updateUserInfo.json'
    print("\nuser info in file "+file_name)
    file_content=read_file(file_name)
    print("\nThe file contents have been read")
    response= update_user_info(file_content,user_id)
    print response.content
    print("\nThe expected status code is "+str(excepted_status_code))
    print("\nThe real status code is " + str(response.status_code))
    assert response.status_code==excepted_status_code
    print("\nThe test_update_user_info is over")