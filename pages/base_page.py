from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на кнопку и ждем изменения URL страницы')
    def click_button_and_wait_url(self, button, url):
        self.driver.find_element(*button).click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Найти и перетащить элемент')
    def click_and_remove_element(self, source_element, target_element):
        if self.driver.capabilities['browserName'] == "firefox":
        # Для Firefox используем пошаговый подход
            ActionChains(self.driver).move_to_element(source_element).click_and_hold().move_to_element(target_element).release().perform()
        else:
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
