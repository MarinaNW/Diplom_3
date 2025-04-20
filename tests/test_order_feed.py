from time import sleep

import allure

from api_methods import ApiMethods
from helpers import Helper
from pages.order_feed_page import OrderFeedPage



class TestOrderFeed:
    @allure.title("Тест при клике на заказ, откроется всплывающее окно с деталями")
    def test_click_on_order(self,driver):

        # Arrange
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open()
        order_feed_page.wait_visibility_of_element()

        # Act
        order_feed_page.click_on_order()
        window_order=order_feed_page.find_window_order()

        # Assert
        assert window_order.is_displayed()


    @allure.title("Тест на то,что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_is_in_order_history_and_in_order_feed(self,driver):
        # Arrange
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()

         # Регистрация пользователя
        create_response = ApiMethods.register_user(email, password, username)
        token = create_response.json().get('accessToken')

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_login_site()
        order_feed_page.login(email, password)
        order_feed_page.wait_element()
        order_feed_page.execute_move_element()
        order_feed_page.click_on_button_place_order()
        sleep(3)
        order_feed_page.wait_visibility_element_cross()
        order_feed_page.click_on_cross_in_order_window()
        order_feed_page.wait_element()
        order_feed_page.click_on_element_personal_account()
        order_feed_page.wait_url_profile_page()
        order_feed_page.click_on_element_order_history()
        order_feed_page.wait_visibility_name_of_order()

        # Act
        found_order=order_feed_page.find_personal_order_on_history_page()
        text = found_order.text

        order_feed_page.click_on_feed_button()
        order_feed_page.wait_visibility_of_element()
        personal_order_feed=order_feed_page.find_personal_order_feed(text)

        # Assert
        assert personal_order_feed.is_displayed()

        # Удаление пользователя
        ApiMethods.delete_user(token)


    @allure.title("Тест - после оформления заказа его номер появляется в разделе В работе»")
    def test_number_order_is_in_work(self, driver):
        # Arrange
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()

        # Регистрация пользователя
        create_response = ApiMethods.register_user(email, password, username)
        token = create_response.json().get('accessToken')

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_login_site()
        order_feed_page.login(email, password)
        order_feed_page.wait_element()

        # Act
        order_feed_page.execute_move_element()
        order_feed_page.click_on_button_place_order()
        order_feed_page.wait_visibility_element_cross()
        sleep(3)
        order_feed_page.find_number_order()
        order_feed_page.click_on_cross_in_order_window()
        order_feed_page.wait_element()
        order_feed_page.click_on_feed_button()
        order_feed_page.wait_visibility_of_element()
        order_number_in_order = order_feed_page.find_personal_order()

        # Assert
        assert order_number_in_order.is_displayed()

        # Удаление пользователя
        ApiMethods.delete_user(token)

    @allure.title("Тест - при создании нового заказа счётчик Выполнено за всё время увеличивается»")
    def test_all_number_order_increase(self, driver):
        # Arrange
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()

        # Регистрация пользователя
        create_response = ApiMethods.register_user(email, password, username)
        token = create_response.json().get('accessToken')

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_login_site()
        order_feed_page.login(email, password)
        order_feed_page.wait_element()

        # Act
        order_feed_page.click_on_feed_button()
        order_feed_page.wait_visibility_of_element()
        initial_order_value =order_feed_page.find_all_number_order()

        order_feed_page.click_on_constructor_button()
        order_feed_page.find_title_base_page()

        order_feed_page.wait_element()
        order_feed_page.execute_move_element()
        order_feed_page.click_on_button_place_order()
        order_feed_page.wait_visibility_element_cross()
        sleep(3)
        order_feed_page.click_on_cross_in_order_window()
        order_feed_page.wait_element()
        order_feed_page.click_on_feed_button()
        order_feed_page.wait_visibility_of_element()
        final_order_value = order_feed_page.find_all_number_order()

        # Assert
        assert final_order_value> initial_order_value

        # Удаление пользователя
        ApiMethods.delete_user(token)



    @allure.title("Тест - при создании нового заказа счётчик Выполнено за день увеличивается»")
    def test_today_number_order_increase(self, driver):
        # Arrange
        email = Helper.generate_email()
        password = Helper.generate_password()
        username = Helper.generate_name()

        # Регистрация пользователя
        create_response = ApiMethods.register_user(email, password, username)
        token = create_response.json().get('accessToken')

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_login_site()
        order_feed_page.login(email, password)
        order_feed_page.wait_element()

        # Act
        order_feed_page.click_on_feed_button()
        order_feed_page.wait_visibility_of_element()
        initial_order_value =order_feed_page.find_today_number_order()


        order_feed_page.click_on_constructor_button()
        order_feed_page.find_title_base_page()

        order_feed_page.wait_element()
        order_feed_page.execute_move_element()
        order_feed_page.click_on_button_place_order()
        order_feed_page.wait_visibility_element_cross()
        sleep(3)
        order_feed_page.click_on_cross_in_order_window()
        order_feed_page.wait_element()
        sleep(1)
        order_feed_page.click_on_feed_button()

        order_feed_page.wait_visibility_of_element()
        final_order_value = order_feed_page.find_today_number_order()

        # Assert
        assert final_order_value> initial_order_value

        # Удаление пользователя
        ApiMethods.delete_user(token)



