import re

import allure

from conftest import driver
from data import Data
from locators.OrderFeedPageLocators import OrderFeedPageLocators


from pages.base_page import BasePage
from urls import Urls


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedPageLocators()

    @allure.step("Открытие страницы Лента Заказов")
    def open(self):
        self.get(Urls.FEED_URL)

    @allure.step("Открытие страницы Авторизации")
    def open_login_site(self):
        self.get(Urls.LOGIN_URL)

    @allure.step("Ожидание видимости заголовка страницы Лента заказов")
    def wait_visibility_of_element(self):
        return self.wait_to_be_visible(self.locators.TITLE_SITE)

    @allure.step("Клик по заказу")
    def click_on_order(self):
        return self.click_on_element(self.locators.ORDER)

    @allure.step("Найти окно заказа")
    def find_window_order(self):
       return self.find_element(self.locators.ORDER_WINDOW)

    @allure.step("Авторизация")
    def login(self, email, password):
        self.fill_input(self.locators.ENTER_EMAIL, email)
        self.fill_input(self.locators.ENTER_PASSWORD, password)
        enter_button = self.wait_to_be_visible(self.locators.ENTER_BUTTON)
        self.js_click_on_element(enter_button)

    @allure.step("Ожидание элемента")
    def wait_element(self):
        return self.wait_to_be_visible(self.locators.ELEMENT)

    @allure.step("Выполнить перетаскивание элемента")
    def execute_move_element(self):
        self.execute_js_drag_and_drop(self.locators.SOURCE_ELEMENT, self.locators.TARGET_ELEMENT)

    @allure.step("Клик по кнопке Оформить заказ")
    def click_on_button_place_order(self):
        return self.click_on_element(self.locators.BUTTON_PLACE_ORDER)

    @allure.step("Закрытие окна оформления заказа по клику на крестик")
    def click_on_cross_in_order_window(self):
        return self.click_on_element(self.locators.CROSS)

    @allure.step("Ожидание видимости элемента Личный кабинет")
    def wait_visibility_personal_account(self):
        return self.wait_to_be_visible(self.locators.PERSONAL_ACCOUNT)

    @allure.step("Клик по элементу Личный кабинет")
    def click_on_element_personal_account(self):
        return self.click_on_element(self.locators.PERSONAL_ACCOUNT)

    @allure.step("Клик по элементу История заказов")
    def click_on_element_order_history(self):
        return self.click_on_element(self.locators.ORDER_HISTORY)

    @allure.step("Изменение URL страницы на PROFILE_URL")
    def wait_url_profile_page(self):
        return self.wait_expected_url(Urls.PROFILE_URL)

    @allure.step("Изменение URL страницы на ORDER_HISTORY_URL")
    def wait_url_order_history_page(self):
        return self.wait_expected_url(Urls.ORDER_HISTORY_URL)

    @allure.step("Ожидание видимости наименования заказа")
    def wait_visibility_name_of_order(self):
         return self.wait_text_to_be_present_in_element(self.locators.ORDER_NAME, Data.NAME_ORDER)

    @allure.step("Найти заказ в истории заказов")
    def find_personal_order_on_history_page(self):
       return self.find_element(self.locators.PERSONAL_ODER)

    @allure.step("Клик по кнопке Лента заказов")
    def click_on_feed_button(self):
        return self.click_on_element(self.locators.ORDER_FEED)

    @allure.step("Найти заказ в ленте заказов")
    def find_personal_order_feed(self, order_number):
        order_locator = self.locators.get_order(order_number)
        return self.find_element(order_locator)

    @allure.step("Ожидание элемента")
    def wait_visibility_element_cross(self):
        return self.wait_text_to_be_present_in_element(self.locators.ORDER_NUMBER_IN_ORDER_WINDOW,Data.FRAGMENT)

    @allure.step("Найти номер заказа в окне оформления заказа")
    def find_number_order(self):
        return self.find_element(self.locators.ORDER_NUMBER_IN_ORDER_WINDOW)

    @allure.step("Найти заказ в работе")
    def find_personal_order(self):
       return self.find_element(self.locators.ORDER_IN_WEEK)

    @allure.step("Клик по кнопке Лента заказов")
    def click_on_feed_button(self):
        return self.click_on_element(self.locators.ORDER_FEED)

    @allure.step("Изменение URL страницы на FEED_URL")
    def wait_url_feed_page(self):
        return self.wait_expected_url(Urls.FEED_URL)

    @allure.step("Найти кол-во выполненных заказов за все время")
    def find_all_number_order(self):
        element =self.find_element(self.locators.ALL_NUMBER_ORDERS)
        value = element.text.strip()
        return value

    @allure.step("Найти кол-во выполненных заказов за день")
    def find_today_number_order(self):
        element =self.find_element(self.locators.TODAY_NUMBER_ORDERS)
        value = element.text.strip()
        return value

    @allure.step("Клик по кнопке Конструктор")
    def click_on_constructor_button(self):
        return self.click_on_element(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Найти название главной страницы Соберите бургер")
    def find_title_base_page(self):
        return self.find_element(self.locators.ELEMENT)
