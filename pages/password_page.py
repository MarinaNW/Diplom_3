import allure

from conftest import driver
from locators.PasswordPageLocators import PasswordPageLocators

from pages.base_page import BasePage
from urls import Urls


class PasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PasswordPageLocators()

    @allure.step("Открытие страницы Восстановления пароля")
    def open(self):
        self.get(Urls.PASSWORD_RECOVERY_URL)


    @allure.step("Открытие страницы Сброс пароля")
    def open_site(self):
        self.get(Urls.RESET_PASSWORD_URL)

    @allure.step("Клик на кнопку Восстановить пароль")
    def click_on_button_recover_password(self):
        self.click_on_element(self.locators.ACCOUNT_LOGIN_BUTTON)
        self.click_on_element(self.locators.RECOVER_PASSWORD_BUTTON)

    @allure.step("Найти название страницы")
    def find_title_page(self):
       return self.find_element(self.locators.RECOVER_PASSWORD)

    @allure.step("Восстановление пароля")
    def recover_password(self,email):
       self.fill_input(self.locators.INPUT_EMAIL, email)
       self.click_on_element(self.locators.RECOVER_BUTTON)

    @allure.step("Изменение изменения URL страницы")
    def wait_url_changed_to_reset_password(self):
        return self.wait_expected_url(Urls.RESET_PASSWORD_URL)

    @allure.step("Найти поле введения пароля")
    def find_field_reset_password(self):
        return self.find_element(self.locators.INPUT_RESET_PASSWORD)


    @allure.step("Клик на кнопку показать/скрыть пароль")
    def click_on_button_show_password(self):
        self.click_on_element(self.locators.SHOW_BUTTON)

    @allure.step("Найти поле введения пароля после клика")
    def find_field_reset_password_after_click(self):
        return self.find_element(self.locators.INPUT_RESET_PASSWORD_AFTER_CLICK)


