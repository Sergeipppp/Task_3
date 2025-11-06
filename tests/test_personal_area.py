from pages.main_page import MainPage
from pages.personal_area_page import PersonalArea
from data import Urls
import allure
import pytest

class TestPersonalArea:
    @allure.title('Проверяем переход в личный кабинет')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_click_to_personal_area_button(self, create_data_for_user, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_personal_area_button_without_login()
        pa = PersonalArea(driver)
        pa.sign_in(create_data_for_user["email"],create_data_for_user["password"])
        main_page.click_personal_area_button_with_login()
        assert driver.current_url == Urls.profile_site

    @allure.title('Проверяем переход к истории заказов в личном кабинете')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_click_to_order_history_button(self, create_data_for_user, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_personal_area_button_without_login()
        pa = PersonalArea(driver)
        pa.sign_in(create_data_for_user["email"],create_data_for_user["password"])
        main_page.click_personal_area_button_with_login()
        pa.click_to_order_history()
        assert driver.current_url == Urls.order_history

    @allure.title('Проверяем выход из аккаунта')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_click_to_logout_button(self, driver, create_data_for_user):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_personal_area_button_without_login()
        pa = PersonalArea(driver)
        pa.sign_in(create_data_for_user["email"],create_data_for_user["password"])
        main_page.click_personal_area_button_with_login()
        pa.click_to_logout_button()
        assert driver.current_url == Urls.login_user
