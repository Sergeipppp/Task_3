from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.orders_list_locators import OrdersListLocators
from pages.base_page import BasePage
import allure

class OrdersList(BasePage):  
    @allure.step('Ждем загрузки ленты заказов')
    def wait_load_orders_list(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrdersListLocators.create_for_all_time))

    @allure.step('Кликнуть на заказ в ленте')
    def click_at_order_in_orders_list(self):
        self.driver.find_element(*OrdersListLocators.order).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrdersListLocators.details_of_order))
