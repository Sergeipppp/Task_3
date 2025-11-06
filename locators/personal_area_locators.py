from selenium.webdriver.common.by import By

class PersonalAreaLocators:
    reset_password_button = (By.XPATH, ".//a[contains(text(),'Восстановить пароль')]")
    input_email = (By.NAME, "name")
    reset_button = (By.XPATH, ".//button[contains(text(),'Восстановить')]")
    hidden_password = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    input_password = (By.XPATH, ".//input[@name='Введите новый пароль']")
    input_pass = (By.XPATH, ".//input[@name='Пароль']")
    sign_in_button = (By.XPATH, ".//button[contains(text(),'Войти')]")
    order_history_button = (By.XPATH, ".//a[contains(text(),'История заказов')]")
    logout_button = (By.XPATH, ".//button[contains(text(),'Выход')]")
    order_number_in_history = (By.CLASS_NAME, "text.text_type_digits-default")
