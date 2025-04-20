from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    # Переход в личный кабинет
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    PROFILE_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")

    # Войти в аккаунт
    ENTER_EMAIL = (By.XPATH, "//input[@name='name']")
    ENTER_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ELEMENT = (By.XPATH, "//h1[text()='Соберите бургер']")


    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    EXIT = (By.XPATH, "//button[text()='Выход']")
