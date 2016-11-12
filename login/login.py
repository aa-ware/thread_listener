#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import getpass
import vk_api # pip3 install vk_api


def two_step_auth_handler():
    code = input("Enter code, which you get by sms: ")
    return code, False


def main():
    email = input("Email\phone number: ")
    password = getpass.getpass()

    vk_session = vk_api.VkApi(email, password, auth_handler=two_step_auth_handler)

    try:
        vk_session.authorization(True)
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    print(vk_session.token)
    # vk = vk_session.get_api()
    # response = vk.wall.get(count=1)  # Используем метод wall.get
    #
    # if response['items']:
    #     print(response['items'][0])
    # token, user_id = auth(email, password, client_id, client_secret)
    # print(token, user_id)


if __name__ == '__main__':
    main()
