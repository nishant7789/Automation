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
CONFIG_PATH = "D:\\Seleniumx\\testdata\\data.json"

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)


class TestLogin(BaseClass):

    def test_logout(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i').click()
        WebDriverWait(self.driver, config["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, '//a[text()="Logout"]'))).click()
        loginpage = LoginPage(self.driver)
        loginpage.get_login_text()
        assert loginpage.get_login_text().is_displayed()
        log.info("Logged out successfully")

    def test_invalid_login(self):
        self.driver.get(config["base_url"])
        WebDriverWait(self.driver, config["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, '//h5[text()="Login"]')))
        print("Login Page displayed")
        self.driver.find_element(By.NAME, 'username').send_keys(config["username"])
        log.info(config["invalid_password"])
        self.driver.find_element(By.NAME, "password").send_keys(config["invalid_password"])
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        invalid_credentials_message = self.driver.find_element(By.CSS_SELECTOR, ".oxd-alert--error").text
        log.info(invalid_credentials_message)
        assert "Invalid" in invalid_credentials_message
