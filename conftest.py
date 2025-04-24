import pytest
from selenium import webdriver

from api_methods import ApiMethods
from helpers import Helper
from urls import Urls


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.get(Urls.BASE_URL)

    yield browser

    browser.quit()


@pytest.fixture(scope="function")
def user_data():
   # Генерация данных пользователя
     email = Helper.generate_email()
     password = Helper.generate_password()
     username = Helper.generate_name()

     # Регистрация пользователя
     response = ApiMethods.register_user(email, password, username)
     token = response.json().get('accessToken')

     yield {
         'email': email,
         'password': password,
         'username': username,
         'token': token
     }

     ApiMethods.delete_user(token)