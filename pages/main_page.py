from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocastors
from pages.base_page import BasePage
from data import Urls
import allure

class MainPage(BasePage):  
    @allure.step('Ждем загрузки булок')
    def wait_load_buns(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocastors.inscription_bread))

    @allure.step('Перейти в личный кабинет без аутентификации')
    def click_personal_area_button_without_login(self):
        self.click_button_and_wait_url(MainPageLocastors.button_personal_area, Urls.login_user)

    @allure.step('Перейти в личный кабинет с аутентификацией')
    def click_personal_area_button_with_login(self):
        self.click_button_and_wait_url(MainPageLocastors.button_personal_area, Urls.profile_site)
    
    @allure.step('Перейти на конструктор')
    def click_construct_button(self):
        self.click_button_and_wait_url(MainPageLocastors.construct_button, Urls.main_site)

    @allure.step('Перейти в ленту заказов')
    def click_orders_list_button(self):
        self.click_button_and_wait_url(MainPageLocastors.orders_list_button, Urls.orders_list)

    @allure.step('Нажать на ингредиент')
    def click_to_ingredient(self):
        self.driver.find_element(*MainPageLocastors.burger).click()

    @allure.step('Закрыть модальное окно с ингредиентом')
    def click_to_close_modal_window_button(self):
        self.driver.find_element(*MainPageLocastors.close_button).click()

    @allure.step('Оформить заказ')
    def click_to_create_order_button(self):
        self.driver.find_element(*MainPageLocastors.create_order_button).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(MainPageLocastors.modal_window_of_order))

    @allure.step('Добавить булку в заказ')
    def add_ingredient_to_order(self):
        self.click_and_remove_element(self.driver.find_element(*MainPageLocastors.burger), self.driver.find_element(*MainPageLocastors.drop))
