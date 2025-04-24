from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
      TITLE_SITE = (By.XPATH, "//h1[text()='Лента заказов']")
      ORDER = (By.XPATH, "//div[@class='OrderHistory_dataBox__1mkxK']")
      ORDER_WINDOW = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")



      ENTER_EMAIL = (By.XPATH, "//input[@name='name']")
      ENTER_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
      ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
      ELEMENT = (By.XPATH, "//h1[text()='Соберите бургер']")
      SOURCE_ELEMENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
      TARGET_ELEMENT = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
      BUTTON_PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

      CROSS = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")


      PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
      ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
      ORDER_BOX = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']")
      ORDER_NAME = (By.XPATH, "//h2[text()='Флюоресцентный бургер']")


      PERSONAL_ODER = (By.XPATH, "//div/p[@class='text text_type_digits-default']")
      ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")



      def get_order(self, text):
            return By.XPATH, f"//p[text()='{text}']"

      ORDER_NUMBER_IN_ORDER_WINDOW = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
      ORDER_IN_WEEK = (By.XPATH, "//li[@class='text text_type_digits-default mb-2']")

      ALL_NUMBER_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::*")
      TODAY_NUMBER_ORDERS =(By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::*")

      CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
