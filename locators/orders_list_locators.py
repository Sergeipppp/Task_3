from selenium.webdriver.common.by import By

class OrdersListLocators:
    create_for_all_time = (By.CSS_SELECTOR, "p[class*='OrderFeed_number__2MbrQ']")
    order = (By.CSS_SELECTOR, "div[class*='OrderHistory_textBox__3lgbs']")
    details_of_order = (By.CLASS_NAME, "text.text_type_main-default.mb-15")
    order_number_in_list = (By.CLASS_NAME, "text.text_type_digits-default")
    create_for_today = (By.XPATH, "/html/body/div/div/main/div/div/div/div[3]/p[2]")
    orders_in_work = (By.XPATH, "//li[@class='text text_type_digits-default mb-2']")
