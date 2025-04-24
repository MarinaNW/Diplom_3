import allure
import requests
from curl import CURL

class ApiMethods:

    @staticmethod
    def register_user(email, password, username):
        with allure.step('Регистрация пользователя'):
            return requests.post(CURL.register_user, json={"email": email,"password": password,"name": username})

    @staticmethod
    def get_user_data(access_token):
        with allure.step('Получение данных пользователя'):
           headers = {'Authorization': f'Bearer+{access_token}'}
           return requests.get(CURL.data_user, headers=headers)


    @staticmethod
    def delete_user(access_token):
        with allure.step("Получение данных об ингредиентах"):
            headers = {'Authorization': f'Bearer+{access_token}'}
            return requests.delete(CURL.delete_user, headers=headers)

    @staticmethod
    def login_user(email, password):
        with allure.step('Авторизация пользователя'):
            return requests.post(CURL.login_user, json={"email": email, "password": password})