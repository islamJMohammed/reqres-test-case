from user_info_class import *


def store_user_info(user_list):
    list = []
    for user in user_list:
        list.append(UserInfo(user['first_name'], user['last_name'], user['id'], user['avatar'],user['email']))

    return list


def read_file(file_name):
    file=open(file_name,"r")
    return file.read()