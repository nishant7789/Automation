import time

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
CONFIG_PATH = "D://Seleniumx//testdata//data.json"

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)


class TestLogin_logout(BaseClass):

    def test_logout(self):
        log.info("Test case 1: Verify if user is able to log out.")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i').click()
        WebDriverWait(self.driver, config["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, '//a[text()="Logout"]'))).click()
        loginpage = LoginPage(self.driver)
        loginpage.get_login_text()
        assert loginpage.get_login_text().is_displayed()
        log.info("Logged out successfully")
    # @pytest.mark.skip(reason="deliberately skipping")
    def test_invalid_login(self):
        self.driver.get(config["base_url"])
        login_page = LoginPage(self.driver)
        WebDriverWait(self.driver, config["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, '//h5[text()="Login"]')))
        print("Login Page displayed")
        login_page.get_username_field().send_keys(config["username"])
        log.info(config["invalid_password"])
        login_page.get_password_field().send_keys(config["invalid_password"])
        login_page.get_submit_btn().click()
        invalid_credentials_message = login_page.get_error_message_invalid_credentials().text
        log.info("The Validation message after wrong Password :{}".format(invalid_credentials_message))
        assert "Invalid" in invalid_credentials_message





