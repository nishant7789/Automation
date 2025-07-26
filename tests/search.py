import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import os
from baseclass.baseclass import BaseClass
from pageobjects.loginpage import LoginPage
logger = BaseClass()
log = logger.getLogger()
# Load config.json
# CONFIG_PATH = "/testdata/search_data.json"
#
# with open(CONFIG_PATH, "r") as config_file:
#     config = json.load(config_file)


# class Test_search(BaseClass):
#
#     def test_search(self):
#         self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i').click()
#         WebDriverWait(self.driver, config["timeout"]).until(
#             EC.presence_of_element_located((By.XPATH, '//a[text()="Logout"]'))).click()
#         loginpage = LoginPage(self.driver)
#         loginpage.get_login_text()
#         assert loginpage.get_login_text().is_displayed()
#         log.info("Logged out successfully")