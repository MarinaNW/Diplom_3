from time import sleep

import allure
from data import Data
from helpers import Helper
from pages.basic_functionality_page import BasicFunctionalityPage


class TestBasicFunctionality:
    @allure.title("Тест перехода по клику на «Конструктор»")
    def test_click_on_constructor_button(self,driver):

        # Arrange
        basic_functionality_page = BasicFunctionalityPage(driver)
        basic_functionality_page.click_on_account_button()
        basic_functionality_page.wait_url_login_page()

        # Act
        basic_functionality_page.click_on_constructor_button()
        title_base_page=basic_functionality_page.find_title_base_page()

        # Assert
        assert title_base_page.is_displayed()



    @allure.title("Тест перехода по клику на «Лента заказов»")
    def test_click_on_feed_button(self,driver):

        # Arrange
        basic_functionality_page = BasicFunctionalityPage(driver)
        basic_functionality_page.click_on_account_button()
        basic_functionality_page.wait_url_login_page()

        # Act
        basic_functionality_page.click_on_feed_button()


        # Assert
        assert basic_functionality_page.wait_url_feed_page()


    @allure.title("Тест появления всплывающего окна с деталям при клике на ингредиент")
    def test_click_on_ingredient(self,driver):

        # Arrange
        basic_functionality_page = BasicFunctionalityPage(driver)

        # Act
        basic_functionality_page.click_on_ingredient()
        details_window = basic_functionality_page.find_details_window()

        # Assert
        assert details_window.is_displayed()


    @allure.title("Тест закрытия всплывающего окна  при клике на крестик")
    def test_click_on_cross(self,driver):

        # Arrange
        basic_functionality_page = BasicFunctionalityPage(driver)

        # Act
        basic_functionality_page.click_on_ingredient()
        details_window = basic_functionality_page.find_details_window()
        basic_functionality_page.click_on_cross()
        basic_functionality_page.wait_disappear_window()

        # Assert
        assert not details_window.is_displayed()


    @allure.title("Тест на увеличение каунтера ингредиента при добавлении ингредиента в заказ")
    def test_increase_counter(self,driver):

        # Arrange
        basic_functionality_page = BasicFunctionalityPage(driver)

        # Act
        basic_functionality_page.find_counter()
        initial_counter_value = basic_functionality_page.get_counter_value()
        basic_functionality_page.execute_move_element()
        basic_functionality_page.find_counter()
        final_counter_value=basic_functionality_page.get_counter_value()

        # Assert
        assert  final_counter_value> initial_counter_value

    @allure.title("Тест на оформление заказа залогиненным пользователем")
    def test_create_order(self, driver):
        # Arrange
        basic_functionality_page = BasicFunctionalityPage(driver)
        basic_functionality_page.open()
        basic_functionality_page.login(Data.EMAIL,Data.PASSWORD)
        basic_functionality_page.wait_element()

        # Act
        basic_functionality_page.execute_move_element()
        basic_functionality_page.click_on_button_place_order()

        assert basic_functionality_page.find_window_order().is_displayed()
