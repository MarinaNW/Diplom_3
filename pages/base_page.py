import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.driver.maximize_window()

    @allure.step("Открытие страницы по url адресу")
    def get(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента")
    def find_element(self, locator):
         return self.driver.find_element(*locator)

    @allure.step("Принудительный клик на элемент")
    def js_click_on_element(self, element):
         self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Поиск и клик на элемент")
    def click_on_element(self, locator):
         self.driver.find_element(*locator).click()

    @allure.step("Поиск элемента и заполнение поля")
    def fill_input(self,locator,text):
         self.driver.find_element(*locator).send_keys(text)

    @allure.step("Ожидание видимости элемента")
    def wait_to_be_visible(self,locator):
         return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))


    @allure.step("Ожидание активации элемента")
    def wait_to_be_clickable(self,locator):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step("Наличия элемента на странице")
    def presence_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))


    @allure.step("Ожидание нужного адреса")
    def wait_expected_url(self,url):
         return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))


    @allure.step("Ожидание когда элемент станет невидимым")
    def wait_to_be_invisible(self,locator):
         return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    @allure.step("Передвижение элемента")
    def move_element(self, locator_source, locator_target):
        source = self.driver.find_element(*locator_source)
        target = self.driver.find_element(*locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()

    @allure.step("Передвижение элемента")
    def execute_js_drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)

        script = """
            var src = arguments[0];  // Исходный элемент
            var tgt = arguments[1];  // Целевой элемент
            var dataTransfer = new DataTransfer();  // Инструмент передачи данных

            // Имитация нажатия кнопки мыши на исходном элементе
            src.dispatchEvent(new MouseEvent('mousedown', {'bubbles': true}));

            // Начало перетаскивания
            src.dispatchEvent(new DragEvent('dragstart', {
                'dataTransfer': dataTransfer,
                'bubbles': true
            }));

            // Этап drop на целевом элементе
            tgt.dispatchEvent(new DragEvent('drop', {
                'dataTransfer': dataTransfer,
                'bubbles': true
            }));

            // Освобождение кнопок мыши
            src.dispatchEvent(new MouseEvent('mouseup', {'bubbles': true}));
        """

        # Передача элементов и выполнение скрипта
        self.driver.execute_script(script, source, target)

    @allure.step("Ожидание когда текст в элементе будет виден")
    def wait_text_to_be_present_in_element(self,locator, text):
         return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))









