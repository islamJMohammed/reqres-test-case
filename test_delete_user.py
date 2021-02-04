from user_services import *


def test_delete_a_user():
    user_id=2
    excepted_status_code = 204
    print("\nThe test_delete_a_user start")
    response=delete_a_user(user_id)
    print("\nThe expected status code is "+str(excepted_status_code))
    print("\nThe real status code is " + str(response.status_code))
    assert response.status_code == excepted_status_code
    print("\nThe test_delete_a_user over")