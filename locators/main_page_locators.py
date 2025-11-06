from selenium.webdriver.common.by import By

class MainPageLocastors:
    button_personal_area = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")
    inscription_bread = (By.XPATH, ".//span[contains(text(),'Булки')]")
    construct_button = (By.XPATH, ".//p[contains(text(),'Конструктор')]")
    orders_list_button = (By.XPATH, ".//p[contains(text(),'Лента Заказов')]")
    burger = (By.CLASS_NAME, "BurgerIngredient_ingredient__1TVf6")
    modal_window = (By.CLASS_NAME, "Modal_modal__title__2L34m")
    close_button = (By.CLASS_NAME, "Modal_modal__close__TnseK")
    make_burger_text = (By.CLASS_NAME, "text_type_main-large")
    create_order_button = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")
    modal_window_of_order = (By.CLASS_NAME, "text_type_main-large")
    order_is_cooking = (By.CLASS_NAME, "text_type_main-small")
    drop = (By.CSS_SELECTOR, "span[class*='constructor-element__row']")
    ingredient_counter = (By.CSS_SELECTOR, "p[class*='counter_counter__num__3nue1']")
    order_number = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
