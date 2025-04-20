import allure
from selenium.webdriver import ActionChains

from conftest import driver
from locators.BasicFunctionalityPageLocators import BasicFunctionalityPageLocators

from pages.base_page import BasePage
from urls import Urls


class BasicFunctionalityPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = BasicFunctionalityPageLocators()

    @allure.step("Открытие страницы Авторизации")
    def open(self):
        self.get(Urls.LOGIN_URL)

    @allure.step("Клик по кнопке Войти в аккаунт")
    def click_on_account_button(self):
        return self.click_on_element(self.locators.ACCOUNT_BUTTON)

    @allure.step("Изменение URL страницы на LOGIN_URL")
    def wait_url_login_page(self):
        return self.wait_expected_url(Urls.LOGIN_URL)

    @allure.step("Клик по кнопке Конструктор")
    def click_on_constructor_button(self):
        return self.click_on_element(self.locators.CONSTRUCTOR_BUTTON)


    @allure.step("Найти название главной страницы Соберите бургер")
    def find_title_base_page(self):
       return self.find_element(self.locators.ELEMENT)

    @allure.step("Клик по кнопке Лента заказов")
    def click_on_feed_button(self):
        return self.click_on_element(self.locators.ORDER_FEED)

    @allure.step("Изменение URL страницы на FEED_URL")
    def wait_url_feed_page(self):
        return self.wait_expected_url(Urls.FEED_URL)

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        return self.click_on_element(self.locators.INGREDIENT)

    @allure.step("Найти окно с деталями")
    def find_details_window(self):
       return self.find_element(self.locators.DETAILS_WINDOW)

    @allure.step("Клик по крестику")
    def click_on_cross(self):
        return self.click_on_element(self.locators.CROSS_BUTTON)


    @allure.step("Ожидание,что окно станет невидимым")
    def wait_disappear_window(self):
        return self.wait_to_be_invisible(self.locators.DETAILS_WINDOW)

    @allure.step("Выполнить перетаскивание элемента")
    def execute_move_element(self):
        # Передача локаторов из файла с локаторами
        self.execute_js_drag_and_drop(self.locators.SOURCE_ELEMENT, self.locators.TARGET_ELEMENT)


    @allure.step("Найти каунтер")
    def find_counter(self):
        return self.find_element(self.locators.COUNTER)

    def get_counter_value(self):
        element = self.find_counter()
        value = element.text.strip()
        return value

    @allure.step("Авторизация")
    def login(self,email,password):
        self.fill_input(self.locators.ENTER_EMAIL, email)
        self.fill_input(self.locators.ENTER_PASSWORD, password)
        enter_button = self.wait_to_be_visible(self.locators.ENTER_BUTTON)
        self.js_click_on_element(enter_button)

    @allure.step("Ожидание элемента")
    def wait_element(self):
        return self.wait_to_be_visible(self.locators.ELEMENT)

    @allure.step("Клик по кнопке Оформить заказ")
    def click_on_button_place_order(self):
        return self.click_on_element(self.locators.BUTTON_PLACE_ORDER)

    @allure.step("Найти окно заказа")
    def find_window_order(self):
        return self.find_element(self.locators.WINDOW_ORDER)