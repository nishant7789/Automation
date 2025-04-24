import json
import logging
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = None


def pytest_addoption(parser):
    """Add CLI options for browser, environment, and country selection."""
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser: chrome, firefox, edge")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            class_name = item.cls.__name__ if item.cls else ""
            file_name = f"Failure_screenshot_{class_name}_{item.name.replace('::', '_')}.png"
            _capture_screenshot('D://Seleniumx//reports//' + file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extras.append(pytest_html.extras.html(html))
        report.extras = extras


def _capture_screenshot(name):

    driver.get_screenshot_as_file(name)


log = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def setup(request):
    """Set up Selenium WebDriver based on config file."""
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--incognito")  # Private browsing mode (no cache)
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(5)
    driver.get(config["base_url"])
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


CONFIG_PATH = "D:\\Seleniumx\\testdata\\data.json"

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)


@pytest.fixture(scope="class")
def login(setup):
    driver = setup

    WebDriverWait(driver, config["timeout"]).until(
        EC.presence_of_element_located((By.XPATH, '//h5[text()="Login"]')))
    print("Login Page displayed")
    driver.find_element(By.NAME, 'username').send_keys(config["username"])
    driver.find_element(By.NAME, "password").send_keys(config["password"])
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    WebDriverWait(driver, config["timeout"]).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text() = 'Dashboard']")))
