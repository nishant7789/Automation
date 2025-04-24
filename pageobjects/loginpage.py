import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CONFIG_PATH = "D:\\Seleniumx\\testdata\\data.json"

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, 'username')
        self.password = (By.NAME, "password")
        self.login_page = (By.XPATH, "//h5[text()='Login']")

    def get_username_field(self):
        return self.driver.find_element(*self.username)

    def get_login_text(self):
        login_text = WebDriverWait(self.driver, config["timeout"]).until(
            EC.presence_of_element_located(self.login_page))
        return login_text
