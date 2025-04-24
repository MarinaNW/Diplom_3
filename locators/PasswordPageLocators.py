from selenium.webdriver.common.by import By

class PasswordPageLocators:
    ACCOUNT_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # вход по кнопке "Войти в аккаунт" на главной
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    RECOVER_PASSWORD= (By.XPATH, "//h2[text() = 'Восстановление пароля']")

    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")


    SHOW_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']/descendant::*[contains(@d,'M12')]")
    INPUT_RESET_PASSWORD = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default']")
    INPUT_RESET_PASSWORD_AFTER_CLICK = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default input_status_active']")