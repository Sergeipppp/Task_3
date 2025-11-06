from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocastors
from pages.personal_area_page import PersonalArea
from data import Urls
import allure
import pytest

class TestMainFunc:
    @allure.title('Проверяем переход в конструктор')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_click_to_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_personal_area_button_without_login()
        main_page.click_construct_button()
        assert driver.current_url == Urls.main_site

    @allure.title('Проверяем переход в ленту заказов')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_click_to_orders_list_button(self, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_orders_list_button()
        assert driver.current_url == Urls.orders_list

    @allure.title('Проверяем всплывающее окно по клику по ингредиенту')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_click_to_ingredients(self, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_to_ingredient()
        assert driver.find_element(*MainPageLocastors.modal_window).text == 'Детали ингредиента'

    @allure.title('Проверяем закрытие всплывающего окна с деталями ингредиента по нажатию крестика')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_click_to_close_modal_window_with_ingredients(self, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_to_ingredient()
        main_page.click_to_close_modal_window_button()
        assert driver.find_element(*MainPageLocastors.make_burger_text).text == 'Соберите бургер'

    @allure.title('Проверяем, что при добавлении ингредиента в заказ, его счетчик увеличивается')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_add_ingredients_in_order(self, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.add_ingredient_to_order()
        assert driver.find_element(*MainPageLocastors.ingredient_counter).text == '2'

    @allure.title('Проверяем, что авторизованный пользователь может создать заказ')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"],
    indirect=True)
    def test_create_order(self, driver, create_data_for_user):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_personal_area_button_without_login()
        pa = PersonalArea(driver)
        pa.sign_in(create_data_for_user["email"],create_data_for_user["password"])
        main_page.click_to_create_order_button()
        assert driver.find_element(*MainPageLocastors.order_is_cooking).text == 'Ваш заказ начали готовить'
