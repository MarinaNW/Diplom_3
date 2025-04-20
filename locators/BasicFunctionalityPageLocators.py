from selenium.webdriver.common.by import By

class BasicFunctionalityPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, "//div/a[@href='/']")  # логотип Stellar Burgers
    ELEMENT_ENTER = (By.XPATH, "// h2[text() = 'Вход']")
    ELEMENT = (By.XPATH, "//h1[text()='Соберите бургер']")

    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    DETAILS_WINDOW = (By.XPATH, "//div[ @class ='Modal_modal__contentBox__sCy8X pt-10 pb-15']")

    CROSS_BUTTON = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']/following-sibling::*")
    SOURCE_ELEMENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    TARGET_ELEMENT =(By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    COUNTER = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']/preceding-sibling::*")

    ENTER_EMAIL = (By.XPATH, "//input[@name='name']")
    ENTER_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")

    BUTTON_PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    WINDOW_ORDER = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
