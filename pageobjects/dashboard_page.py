import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CONFIG_PATH = "D://Seleniumx//testdata//data.json"

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.XPATH, '//input[@placeholder="Search"]')
        self.result = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span')

    def search(self, search_text):
        search_input = WebDriverWait(self.driver, config["timeout"]).until(
            EC.presence_of_element_located(self.search_field))
        search_input.clear()
        search_input.send_keys(search_text)
        # search_input.send_keys("Leave")
        result = WebDriverWait(self.driver, config["timeout"]).until(
            EC.presence_of_element_located(self.result))
