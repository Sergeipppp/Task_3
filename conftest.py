import pytest
from selenium import webdriver
from helpers import MakeTestData
from data import Urls
import requests

class BrowserFactory:
    @staticmethod
    def getWebdriver(browserName):
        if browserName == "chrome":
            return webdriver.Chrome()
        elif browserName == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browserName}")

@pytest.fixture
def driver(request):
    browser_name = request.param
    driver = BrowserFactory.getWebdriver(browser_name)
    driver.get(Urls.main_site)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def create_data_for_user():
    email = MakeTestData.generate_random_string(10)
    password = MakeTestData.generate_random_string(10)
    name = MakeTestData.generate_random_string(10)

    payload = {
        "email": f"{email}@yandex.ru",
        "password": password,
        "name": name
    }
    response = requests.post(Urls.register_user, data=payload)
    headers = {
        "Authorization": response.json()["accessToken"],
        "Content-Type": "application/json"
    }
    yield payload
    requests.delete(Urls.user, json=payload, headers=headers)
