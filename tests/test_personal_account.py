

import allure
from data import Data

from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.title("Тест перехода на страницу Личный кабинет по клику")
    def test_click_on_personal_account(self,driver):

        # Arrange
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open()
        personal_account_page.login(Data.EMAIL,Data.PASSWORD)

        # Act
        personal_account_page.wait_element()
        personal_account_page.click_on_element_personal_account()

        # Assert
        assert personal_account_page.wait_url_profile_page()


    @allure.title("Тест перехода на страницу История заказов по клику")
    def test_click_on_order_history(self,driver):

        # Arrange
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open()
        personal_account_page.login(Data.EMAIL,Data.PASSWORD)
        personal_account_page.wait_element()
        personal_account_page.click_on_element_personal_account()

        # Act
        personal_account_page.wait_url_profile_page()
        personal_account_page.click_on_element_order_history()

        # Assert
        assert personal_account_page.wait_url_order_history_page()

    @allure.title("Тест выход из личного кабинета")
    def test_logout_from_personal_account(self, driver):
        # Arrange
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open()
        personal_account_page.login(Data.EMAIL, Data.PASSWORD)

        personal_account_page.wait_element()
        personal_account_page.click_on_element_personal_account()

        # Act
        personal_account_page.wait_url_profile_page()
        personal_account_page.click_on_element_exit()

        # Assert
        assert personal_account_page.wait_url_login_page()


