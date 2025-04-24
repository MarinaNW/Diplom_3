
import allure
from data import Data

from pages.password_page import PasswordPage


class TestPassword:
    @allure.title("Тест перехода на страницу восстановления пароля по кнопке Восстановить пароль")
    def test_button_recover_password(self,driver):
        # Arrange
        password_page = PasswordPage(driver)

        # Act
        password_page.click_on_button_recover_password()
        page_title = password_page.find_title_page()

        # Assert
        assert page_title.is_displayed()

    @allure.title("Тест ввода почты и клик по кнопке Восстановить")
    def test_button_recover(self, driver):
        # Arrange
        password_page = PasswordPage(driver)
        password_page.click_on_button_recover_password()
        password_page.find_title_page()

        # Act
        password_page.recover_password(Data.NEW_EMAIL)

        #Assert
        assert password_page.wait_url_changed_to_reset_password()



    def test_show_button(self, driver):
        # Arrange
        password_page = PasswordPage(driver)
        password_page.click_on_button_recover_password()
        password_page.find_title_page()
        password_page.recover_password(Data.NEW_EMAIL)
        password_page.wait_url_changed_to_reset_password()

        # Act
        password_field = password_page.find_field_reset_password()
        original_class = password_field.get_attribute('class')  # Сохраняем исходный класс
        password_page.click_on_button_show_password()

        # Assert
        # Подтверждаем изменение класса
        assert original_class != password_field.get_attribute('class')
