import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import os

from baseclass.baseclass import BaseClass
from pageobjects import dashboard_page
from pageobjects.dashboard_page import DashboardPage

logger = BaseClass()
log = logger.getLogger()
# Load config.json
CONFIG_PATH = "D://Seleniumx//testdata//search_data.json"

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)


class TestDashboard(BaseClass):

    def test_search(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.search(config["search_query"])
        result = WebDriverWait(self.driver, config["timeout"]).until(
            EC.presence_of_element_located(dashboard_page.result))
        print("Search result text:", result.text)
        assert result.text == "Leave"
