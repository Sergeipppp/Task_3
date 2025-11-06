from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.personal_area_locators import PersonalAreaLocators
from data import Urls
import allure

class PersonalArea(BasePage):
    @allure.step('Кликнуть по кнопке восстановить пароль')
    def click_to_reset_password_button(self):
        self.click_button_and_wait_url(PersonalAreaLocators.reset_password_button, Urls.forgot_password)

    @allure.step('Ввести email для восстановления пароля')
    def input_email_for_reset_password(self, email):
        self.driver.find_element(*PersonalAreaLocators.input_email).send_keys(email)
        self.click_button_and_wait_url(PersonalAreaLocators.reset_button, Urls.reset_password)

    @allure.step('Восстановить пароль')
    def reset_password(self, email):
        self.click_to_reset_password_button()
        self.input_email_for_reset_password(email)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.input_password))

    @allure.step('Скрыть или показать пароль')
    def hidden_password(self):
        self.driver.find_element(*PersonalAreaLocators.hidden_password).click()
        
    @allure.step('Перейти в историю заказов')
    def click_to_order_history(self):
        self.click_button_and_wait_url(PersonalAreaLocators.order_history_button, Urls.order_history)

    @allure.step('Перейти в историю заказов и подождать загрузки заказов')
    def click_to_order_history_and_wait_orders(self):
        self.click_button_and_wait_url(PersonalAreaLocators.order_history_button, Urls.order_history)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.order_number_in_history))
    
    @allure.step('Выход из аккаунта')
    def click_to_logout_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PersonalAreaLocators.logout_button))
        self.click_button_and_wait_url(PersonalAreaLocators.logout_button, Urls.login_user)

    @allure.step('Зайти в аккаунт под определенным пользователем')
    def sign_in(self, email, password):
        self.driver.find_element(*PersonalAreaLocators.input_email).send_keys(email)
        self.driver.find_element(*PersonalAreaLocators.input_pass).send_keys(password)
        self.click_button_and_wait_url(PersonalAreaLocators.sign_in_button, Urls.main_site)
