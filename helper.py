from user_info_class import *
from user_services import *
from jsonpath import jsonpath

import json


def store_user_info(user_list):
    list = []
    for user in user_list:
        list.append(UserInfo(user['first_name'], user['last_name'], user['id'], user['avatar'], user['email']))

    return list


def read_file(file_name):
    file = open(file_name, "r")
    return file.read()


def get_user_info(page):
    response = get_users_list(page)
    json_text = json.loads(response.text)
    data = jsonpath(json_text, 'data')
    return data, response


def get_list_of_users():
    page = 1
    all_users = []
    data, response = get_user_info(page)
    while len(data[0]) > 0:
        all_users = all_users + data[0]
        page = page + 1
        data = get_user_info(page)
    list = store_user_info(all_users)
    return list, response


def create_user(file_name):
    file_content = read_file(file_name)
    return create_new_user(file_content)


def update_user(file_name, user_id):
    file_content = read_file(file_name)
    return update_user_info(file_content, user_id)


def delete_user(user_id):
    return delete_a_user(user_id)
