import requests
import json

# VARIABLES PART
BASE_URL="https://reqres.in"

#GET URL
GET_USERS_LIST_URL="/api/users?page=2"
GET_SINGLE_USER_URL="/api/users/"
GET_SINGLE_USER_NOT_FOUND_URL="/api/users/"
#POST URL
POST_CREATE_USER_URL="/api/users"
#DELETE URL
DELETE_A_USER_URL="/api/users/"
#PUT URL
UPDATE_USER_INFO="/api/users/"



#GET  USERS METHODS

#GET LIST OF USERS
def get_users_list():
    return requests.get(BASE_URL+GET_USERS_LIST_URL)

#GET SINGLE USER
def get_single_user(user_id):
    return requests.get(BASE_URL+GET_SINGLE_USER_URL+str(user_id))

#GET SINGLE USER NOT FOUND
def get_single_user_not_found(user_id):
    return requests.get(BASE_URL+GET_SINGLE_USER_NOT_FOUND_URL+str(user_id))

#POST  USERS METHODS

#CREATE NEW USER
def create_new_user(new_user_data):
    json_content = json.loads(new_user_data)
    return requests.post(BASE_URL+POST_CREATE_USER_URL, json_content)



#DELETE USER METHODS

#DELETE A USER
def delete_a_user(user_id):
    return requests.delete(BASE_URL+DELETE_A_USER_URL+str(user_id))


#PUT USER METHODS
def update_user_info(user_data,user_id):
    json_content = json.loads(user_data)
    return requests.post(BASE_URL+UPDATE_USER_INFO+str(user_id), json_content)


