from pages.main_page import MainPage
from pages.orders_list import OrdersList
from locators.orders_list_locators import OrdersListLocators
from locators.main_page_locators import MainPageLocastors
from locators.personal_area_locators import PersonalAreaLocators
from pages.personal_area_page import PersonalArea
from selenium.webdriver.support.wait import WebDriverWait
import allure
import pytest

class TestOrdersList:
    @allure.title('Проверяем всплывающее окно с деталями о заказе')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_click_and_get_details_of_order(self, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_orders_list_button()
        order_list = OrdersList(driver)
        order_list.wait_load_orders_list()
        order_list.click_at_order_in_orders_list()
        assert driver.find_element(*OrdersListLocators.details_of_order).text == "Выполнен"

    @allure.title('Проверяем, что созданный заказ будет в истории заказов и в ленте заказов')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_create_order_and_find_it_in_order_history_and_orders_list(self, create_data_for_user, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_personal_area_button_without_login()
        pa = PersonalArea(driver)
        pa.sign_in(create_data_for_user["email"],create_data_for_user["password"])
        main_page.add_ingredient_to_order()
        main_page.click_to_create_order_button()
        initial_text = driver.find_element(*MainPageLocastors.order_number).text
        WebDriverWait(driver, 10).until(lambda driver:driver.find_element(*MainPageLocastors.order_number).text != initial_text)
        order_number = driver.find_element(*MainPageLocastors.order_number).text
        main_page.click_to_close_modal_window_button()
        main_page.click_personal_area_button_with_login()
        pa.click_to_order_history_and_wait_orders()
        assert driver.find_element(*PersonalAreaLocators.order_number_in_history).text[2:] == order_number
        main_page.click_orders_list_button()
        order_list = OrdersList(driver)
        order_list.wait_load_orders_list()
        list_of_elements = driver.find_elements(*OrdersListLocators.order_number_in_list)
        list_of_elements_text = []
        for i in list_of_elements:
            list_of_elements_text.append(i.text[2:])
        assert order_number in list_of_elements_text

    @allure.title('Проверяем, что при создании нового заказа счётчик выполнено за всё время увеличивается')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_create_order_and_check_ready_for_all_time_orders_counter(self, create_data_for_user, driver):   
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_orders_list_button()
        order_list = OrdersList(driver)
        order_list.wait_load_orders_list()
        created_order = driver.find_element(*OrdersListLocators.create_for_all_time).text
        main_page.click_personal_area_button_without_login()
        pa = PersonalArea(driver)
        pa.sign_in(create_data_for_user["email"],create_data_for_user["password"])
        main_page.add_ingredient_to_order()
        main_page.click_to_create_order_button()
        initial_text = driver.find_element(*MainPageLocastors.order_number).text
        WebDriverWait(driver, 10).until(lambda driver:driver.find_element(*MainPageLocastors.order_number).text != initial_text)
        main_page.click_to_close_modal_window_button()
        main_page.click_orders_list_button()
        order_list.wait_load_orders_list()
        assert int(driver.find_element(*OrdersListLocators.create_for_all_time).text) == int(created_order) + 1

    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_create_order_and_check_ready_for_today_orders_counter(self, create_data_for_user, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_orders_list_button()
        order_list = OrdersList(driver)
        order_list.wait_load_orders_list()
        created_order_today = driver.find_element(*OrdersListLocators.create_for_today).text
        main_page.click_personal_area_button_without_login()
        pa = PersonalArea(driver)
        pa.sign_in(create_data_for_user["email"],create_data_for_user["password"])
        main_page.add_ingredient_to_order()
        main_page.click_to_create_order_button()
        initial_text = driver.find_element(*MainPageLocastors.order_number).text
        WebDriverWait(driver, 10).until(lambda driver:driver.find_element(*MainPageLocastors.order_number).text != initial_text)
        main_page.click_to_close_modal_window_button()
        main_page.click_orders_list_button()
        order_list.wait_load_orders_list()
        assert int(driver.find_element(*OrdersListLocators.create_for_today).text) == int(created_order_today) + 1

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе в работе')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_create_order_and_check_it_in_section_in_work(self, create_data_for_user, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_personal_area_button_without_login()
        pa = PersonalArea(driver)
        pa.sign_in(create_data_for_user["email"],create_data_for_user["password"])
        main_page.add_ingredient_to_order()
        main_page.click_to_create_order_button()
        initial_text = driver.find_element(*MainPageLocastors.order_number).text
        WebDriverWait(driver, 10).until(lambda driver:driver.find_element(*MainPageLocastors.order_number).text != initial_text)
        order_number = driver.find_element(*MainPageLocastors.order_number).text
        main_page.click_to_close_modal_window_button()
        main_page.click_orders_list_button()
        order_list = OrdersList(driver)
        order_list.wait_load_orders_list()
        assert driver.find_element(*OrdersListLocators.orders_in_work).text[1:] == order_number
