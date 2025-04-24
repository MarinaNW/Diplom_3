import allure
from locators.PersonalAccountPageLocators import PersonalAccountPageLocators

from pages.base_page import BasePage
from urls import Urls


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PersonalAccountPageLocators()

    @allure.step("Открытие страницы Авторизации")
    def open(self):
        self.get(Urls.LOGIN_URL)


    @allure.step("Авторизация")
    def login(self,email,password):
        self.fill_input(self.locators.ENTER_EMAIL, email)
        self.fill_input(self.locators.ENTER_PASSWORD, password)
        enter_button = self.wait_to_be_visible(self.locators.ENTER_BUTTON)
        self.js_click_on_element(enter_button)

    @allure.step("Клик по элементу Личный кабинет")
    def click_on_element_personal_account(self):
        return self.click_on_element(self.locators.PERSONAL_ACCOUNT)

    @allure.step("Клик по элементу История заказов")
    def click_on_element_order_history(self):
        return self.click_on_element(self.locators.ORDER_HISTORY)


    @allure.step("Клик по элементу Выход")
    def click_on_element_exit(self):
        return self.click_on_element(self.locators.EXIT)


    @allure.step("Изменение URL страницы на PROFILE_URL")
    def wait_url_profile_page(self):
        return self.wait_expected_url(Urls.PROFILE_URL)

    @allure.step("Изменение URL страницы на ORDER_HISTORY_URL")
    def wait_url_order_history_page(self):
        return self.wait_expected_url(Urls.ORDER_HISTORY_URL)

    @allure.step("Изменение URL страницы на LOGIN_URL")
    def wait_url_login_page(self):
        return self.wait_expected_url(Urls.LOGIN_URL)


    @allure.step("Ожидание элемента")
    def wait_element(self):
         return self.wait_to_be_visible(self.locators.ELEMENT)








