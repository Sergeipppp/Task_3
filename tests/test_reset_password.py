from pages.main_page import MainPage
from pages.personal_area_page import PersonalArea
from locators.personal_area_locators import PersonalAreaLocators
from data import Urls
import allure
import pytest

class TestResetPassword:
    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_click_to_reset_password_button(self, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_personal_area_button_without_login()  
        pa = PersonalArea(driver)
        pa.click_to_reset_password_button()
        assert driver.current_url == Urls.forgot_password

    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_input_email_and_click_reset_button(self, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_personal_area_button_without_login()  
        pa = PersonalArea(driver)
        pa.click_to_reset_password_button()
        pa.input_email_for_reset_password("sss@mail.ru")
        assert driver.current_url == Urls.reset_password

    @allure.title('Проверяем полный функционал восстановления пароля')
    @pytest.mark.parametrize(
    "driver", 
    ["chrome", "firefox"], 
    indirect=True)
    def test_reset_password(self, driver):
        main_page = MainPage(driver)
        main_page.wait_load_buns()
        main_page.click_personal_area_button_without_login()
        pa = PersonalArea(driver)
        pa.reset_password("sss@mail.ru")
        pa.hidden_password()
        element = driver.find_element(*PersonalAreaLocators.input_password)
        assert element.get_attribute("type") == "text"
